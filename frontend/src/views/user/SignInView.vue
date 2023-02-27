<template>
    <div class="flex min-h-full flex-col justify-center sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <h1 class="text-3xl font-bold tracking-tight mb-10">Sign In</h1>
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                <form class="space-y-6" @submit.prevent="signIn">
                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                        <div class="mt-1">
                            <input @change="errors.username = null" id="email" v-model="logUser.username"
                                autocomplete="email" type="text"
                                :class="'field ' + (errors.username ? 'field-error' : '')" />
                        </div>
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                        <div class="mt-1">
                            <input @change="errors.password = null" id="password" v-model="logUser.password"
                                autocomplete="current-password" type="password"
                                :class="'field ' + (errors.password ? 'field-error' : '')" />
                        </div>
                    </div>

                    <div v-if="errors.auth" class="text-red-600">{{ errors.auth }}</div>

                    <div class="flex items-center justify-right">
                        <div class="text-sm">
                            <RouterLink to="/reset-password" class="font-medium text-gray-800 hover:text-gray-600">
                                Forgot your password?
                            </RouterLink>
                        </div>
                    </div>

                    <div>
                        <ButtonWithSpinner :loading="isLoading" text="Sign in"></ButtonWithSpinner>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { userStore } from '../../stores/user'

export default {
    data() {
        return {
            logUser: {
                username: "",
                password: "",
            },

            errors: {},

            isLoading: false,
        };
    },
    methods: {
        async signIn() {

            this.isLoading = true
            this.errors = {}

            this.axios
                .post(this.apiUrl + "users/sign-in/", this.logUser,
                    {
                        headers: {
                            "Content-type": "multipart/form-data",
                        }
                    }
                )
                .then(response => {
                    userStore().setUser(response.data)
                    this.axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`
                    this.$router.push('/')
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
        }
    }
}
</script>