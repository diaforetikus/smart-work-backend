<template>
    <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
        <div class="flex min-h-full flex-col justify-center sm:px-6 lg:px-8">
            <div class="sm:mx-auto sm:w-full sm:max-w-md">
                <h1 class="text-3xl font-bold tracking-tight mb-10">Forgot your password</h1>
                <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                    <form class="space-y-6" @submit.prevent="signIn">
                        <div>
                            <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                            <div class="mt-1">
                                <input @change="errors.email = null" id="email" v-model="user.email"
                                    autocomplete="email" type="text"
                                    :class="'field ' + (errors.email ? 'field-error' : '')" />
                            </div>
                        </div>

                        <div v-if="errors.user" class="text-red-600">{{ errors.user }}</div>

                        <div>
                            <ButtonWithSpinner :loading="isLoading" text="Reset"></ButtonWithSpinner>
                        </div>
                    </form>
                </div>
            </div>
            <Modal :show="showSuccessModal" @closed="closed" title="We send e-mail with instructions to you"></Modal>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                email: "",
            },

            errors: {},

            showSuccessModal: false,

            isLoading: false
        };
    },

    methods: {
        signIn() {
            this.isLoading = true
            this.errors = {}

            this.axios
                .post(this.apiUrl + "users/reset-password/", this.user)
                .then(response => {
                    this.user.email = ''
                    this.showSuccessModal = true
                })
                .catch(error => {
                    if (error.response.data.detail[0].loc) {
                        error.response.data.detail.forEach((item) => {
                            this.errors[item.loc[1]] = item.msg
                        })
                    }
                    else {
                        this.errors["user"] = error.response.data.detail
                    }
                })
                .finally(() => {
                    this.isLoading = false
                })
        },

        closed()
        {
            this.showSuccessModal = false
        }
    }
}
</script>