<template>
    <div class="flex min-h-full flex-col justify-center sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <h1 class="text-3xl font-bold tracking-tight mb-10">Sign Up</h1>
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                <form class="space-y-6" @submit.prevent="signUp">

                    <div>
                        <label for="first_name" class="block text-sm font-medium text-gray-700">First name</label>
                        <div class="mt-1">
                            <input @change="errors.first_name = null" id="first_name" v-model="user.first_name"
                                name="first_name" type="text"
                                :class="'field ' + (errors.first_name ? 'field-error' : '')" />
                        </div>
                    </div>

                    <div>
                        <label for="last_name" class="block text-sm font-medium text-gray-700">Last name</label>
                        <div class="mt-1">
                            <input @change="errors.last_name = null" id="last_name" v-model="user.last_name"
                                name="last_name" type="text"
                                :class="'field ' + (errors.last_name ? 'field-error' : '')" />
                        </div>
                    </div>

                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                        <div class="mt-1">
                            <input @change="errors.email = null" id="email" v-model="user.email" name="email"
                                type="text" autocomplete="email"
                                :class="'field ' + (errors.email ? 'field-error' : '')" />
                        </div>
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                        <div class="mt-1">
                            <input @change="errors.password = null" id="password" v-model="user.password"
                                name="password" type="password" autocomplete="current-password"
                                :class="'field ' + (errors.password ? 'field-error' : '')" />
                        </div>
                    </div>

                    <div v-if="errors.auth" class="text-red-600">{{ errors.auth }}</div>

                    <div>
                        <ButtonWithSpinner :loading="isLoading" text="Sign up"></ButtonWithSpinner>
                    </div>
                </form>
            </div>
        </div>
        <Modal :show="showSuccessModal" @closed="closed" title="Registration successfull">
        </Modal>
    </div>
</template>

<script>
import { userStore } from '../../stores/user'

export default {
    data() {
        return {
            user: {
                email: "",
                first_name: "",
                last_name: "",
                password: ""
            },

            showSuccessModal: false,

            errors: {},

            isLoading: false,
        };
    },
    methods: {
        async signUp() {

            this.isLoading = true
            this.errors = {}

            this.axios
                .post(this.apiUrl + "users/sign-up/", this.user)
                .then(response => {
                    userStore().setUser(response.data)
                    this.axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`
                    this.showSuccessModal = true
                })
                .catch(error => {
                    if (error.response.data.detail[0].loc) {
                        error.response.data.detail.forEach((item) => {
                            this.errors[item.loc[1]] = item.msg.charAt(0).toUpperCase() + item.msg.slice(1)
                        })
                    }
                    else {
                        this.errors["auth"] = error.response.data.detail
                    }
                })
                .finally(() => {
                    this.isLoading = false
                })
        },

        closed() {
            this.showSuccessModal = false
            this.$router.push('/')
        }
    }
}
</script>