<template>
    <div>
        <div v-if="user" class="bg-white px-6 pt-6 pb-6 shadow rounded-lg flex flex-col">
            <form class="space-y-4">
                <div>
                    <label for="user-email" class="label">
                        E-mail
                    </label>
                    <div class="mt-1">
                        <input v-model="user.email" @change="errors.email = null" id="user-email" name="email" type="text"
                               :class="'field '+ (errors.email ? 'field-error' : '')">
                    </div>
                    <p v-if="errors.email" class="mt-2 text-sm text-red-600">{{ errors.email }}</p>
                </div>
                <div class="flex justify-end">
                    <ButtonWithSpinner @click="updateEmail" :loading="isLoading" text="Update"></ButtonWithSpinner>
                </div>
            </form>

             
        </div>

        <Modal :show="showSuccessModal" @closed="showSuccessModal = false" title="Your email has been changed!">
        </Modal>
    </div>
</template>

<script>

    import { userStore } from '../../stores/user'
    import LoadingIcon from "../icons/LoadingIcon.vue"

    export default {
        components: {
            LoadingIcon
        },

        props: [],

        data() {
            return {
                menu: '',
                user: null,
                isLoading: false,
                errors: {},
                url: '/api/users/',
                showSuccessModal: false,
                newImage: null
            }
        },

        mounted() {
            this.user = userStore().user
        },

        methods: {
            updateEmail() {
                this.isLoading = true
                this.errors = {}

                let payload = {
                    email: this.user.email
                }

                this.axios
                    .patch(this.apiUrl + 'users/update-email', payload)
                    .then(response => {
                        userStore().setUser(response.data)
                        this.axios.defaults.headers.common['Authorization'] = `Bearer ${this.user.token}`
                        this.showSuccessModal = true
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
        }
    }
</script>