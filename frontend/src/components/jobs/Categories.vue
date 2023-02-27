<template>
    <Combobox as="div" v-model="selectedCategory">
        <div class="relative">
            <ComboboxInput :class="'field ' + (error ? 'field-error' : '')" @change="query = $event.target.value" placeholder="Select category" :display-value="(category) => category?.name" />
            <ComboboxButton class="absolute inset-y-0 right-0 flex items-center rounded-r-md px-2 focus:outline-none">
                <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
            </ComboboxButton>

            <transition
                enter-active-class="transition duration-100 ease-out"
                enter-from-class="transform scale-95 opacity-0"
                enter-to-class="transform scale-100 opacity-100"
                leave-active-class="transition duration-75 ease-out"
                leave-from-class="transform scale-100 opacity-100"
                leave-to-class="transform scale-95 opacity-0"
            >
                <ComboboxOptions v-if="filteredCategories.length > 0" class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                    <ComboboxOption v-for="category in filteredCategories" :key="category.id" :value="category" @click="selected" as="template" v-slot="{ active, selected }">
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
            </transition>
        </div>
    </Combobox>
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

                categories: [
                    {"id": 0, "name": "All categories"},
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

                selectedCategory: null,

                error: false
            }
        },

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

        methods: {
            selected() {

                let data = this.selectedCategory
                if (this.selectedCategory.id === 0)
                    data = null

                this.$emit("selected", data)
            }
        }
    }
</script>