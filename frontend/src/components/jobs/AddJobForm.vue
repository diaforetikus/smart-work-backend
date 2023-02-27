<template>
<form @submit.prevent="addJob" class="space-y-4">
    <div>
        <div class="flex">
            <label for="category" class="label mr-2">Job category</label>
            <div v-if="errors.category_id" class="text-sm text-red-600">Select category</div>
        </div>
        <Combobox as="div" v-model="job.category">
            <div class="relative">
            <ComboboxInput :class="'field ' + (errors.category_id ? 'field-error' : '')" @change="query = $event.target.value" :display-value="(category) => category?.name" />
            <ComboboxButton class="absolute inset-y-0 right-0 flex items-center rounded-r-md px-2 focus:outline-none">
                <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
            </ComboboxButton>

            <ComboboxOptions v-if="filteredCategories.length > 0" class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                <ComboboxOption v-for="category in filteredCategories" :key="category.id" :value="category" as="template" v-slot="{ active, selected }">
                <li :class="['relative cursor-default select-none py-2 pl-8 pr-4', active ? 'bg-gray-100' : '']">
                    <span :class="['block truncate', selected && 'font-semibold']">
                        {{ category.name }}
                    </span>
                    <span v-if="selected" :class="['absolute inset-y-0 left-0 flex items-center pl-1.5', active ? 'text-black' : 'text-black']">
                        <CheckIcon class="h-5 w-5" aria-hidden="true" />
                    </span>
                </li>
                </ComboboxOption>
            </ComboboxOptions>
            </div>
        </Combobox>
    </div>
    <div>
        <div class="flex">
            <label for="title" class="label mr-2">Job title</label>
            <div v-if="errors.title" class="text-sm text-red-600">{{ errors.title }}</div>
        </div>
        <input v-model="job.title" id="title" :class="'field ' + (errors.title ? 'field-error' : '')" type="text" placeholder="Enter job title" />
    </div>
    <div>
        <div class="flex">
            <label for="amount" class="label mr-2">$ Amount</label>
            <div v-if="errors.amount" class="text-sm text-red-600">{{ errors.amount }}</div>
        </div>
        <input v-model="job.amount" id="amount" :class="'field ' + (errors.amount ? 'field-error' : '')" type="text" placeholder="Enter amount" />
    </div>
    <div>
        <div class="flex">
            <label for="description" class="label mr-2">Job description</label>
            <div v-if="errors.description" class="text-sm text-red-600">{{ errors.description }}</div>
        </div>
        <textarea v-model="job.description" id="description"  :class="'field h-96 ' + (errors.description ? 'field-error' : '')" placeholder="Enter job description"></textarea>
    </div>
    <div class="flex justify-end">
        <ButtonWithSpinner :loading="isLoading" text="Add job"></ButtonWithSpinner>
    </div>
</form>
<Teleport to="body">
    <Modal :show="showSuccessModal" @closed="closed" title="Job has been added!">
    </Modal>
</Teleport>
</template>

<script>
    import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'
    import {
        Combobox,
        ComboboxButton,
        ComboboxInput,
        ComboboxOption,
        ComboboxOptions,
    } from '@headlessui/vue' 

    export default {
        components: {
            CheckIcon,
            ChevronUpDownIcon,
            Combobox,
            ComboboxButton,
            ComboboxInput,
            ComboboxOption,
            ComboboxOptions,
        },

        data() {
            return {
                query: '',

                job: {
                    'id': null,
                    'title': '',
                    'description': '',
                    'amount': null,
                    'category': null,
                    'category_id': null,
                },

                categories: [
                    {"id": 1, "name": "Software Development"},
                    {"id": 2, "name": "Network Administration"},
                    {"id": 3, "name": "Systems Administration"},
                    {"id": 4, "name": "Database Administration"},
                    {"id": 5, "name": "Cloud Computing"},
                    {"id": 6, "name": "Cybersecurity"},
                    {"id": 7, "name": "Web Development"},
                    {"id": 8, "name": "Information Technology Support"},
                    {"id": 9, "name": "Software Quality Assurance"},
                    {"id": 10, "name": "Data Science"},
                    {"id": 11, "name": "Business Intelligence"},
                    {"id": 12, "name": "Mobile Application Development"},
                    {"id": 13, "name": "Marketing"},
                ],

                isLoading: false,

                errors: {},

                showSuccessModal: false
            }
        },

        emits: ["added"],

        computed: {
            filteredCategories() {
                if (this.query === '')
                    return this.categories.slice(0, 100)
                else
                {
                    return this.categories.filter((category) => {
                        return category.name.toLowerCase().includes(this.query.toLowerCase())
                    }).slice(0, 100)
                }
            }
        },

        mounted() {
           
        },

        methods: {
            addJob() 
            {
                this.isLoading = true
                this.errors = {}

                if (this.job.category)
                    this.job.category_id = this.job.category.id

                this.axios
                    .post(this.apiUrl + 'jobs', this.job)
                    .then(response => {
                        this.showSuccessModal = true

                        this.job.id = response.data.id
                        this.job.title = ''
                        this.job.description = ''
                        this.job.amount = null
                        this.job.category = null
                        this.job.category_id = null
                    })
                    .catch(error => {
                        if (error.response.data.detail[0].loc) {
                            error.response.data.detail.forEach((item) => {
                                this.errors[item.loc[1]] = item.msg.charAt(0).toUpperCase() + item.msg.slice(1)
                            })
                        }
                    })
                    .finally(() => {
                        this.isLoading = false
                    })
            },

            closed()
            {
                this.showSuccessModal = false
                this.$router.push('/jobs/' + this.job.id)
            }
        }
    }
</script>
