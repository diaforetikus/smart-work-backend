<template>
    <div>
        <div class="bg-white px-6 pt-6 pb-6 shadow rounded-lg">
            <form class="space-y-4">
                <div>
                    <label for="password" class="label">
                        Current password
                    </label>
                    <div class="mt-1">
                        <input v-model="password" @change="errors.password = null" id="password" name="password" type="password"
                               placeholder="Enter current password "
                               :class="'field '+ (errors.password ? 'field-error' : '')">
                    </div>
                    <p v-if="errors.password" class="mt-2 text-sm text-red-600">{{ errors.password }}</p>
                </div>

                <div>
                    <label for="new_password" class="label">
                        New password
                    </label>
                    <div class="mt-1">
                        <input v-model="new_password"  @change="errors.new_password = null" id="new_password" name="new_password" type="password"
                               placeholder="Enter new password "
                               :class="'field '+ (errors.new_password ? 'field-error' : '')">
                    </div>
                    <p v-if="errors.new_password" class="mt-2 text-sm text-red-600">{{ errors.new_password }}</p>
                </div>
                <div class="flex justify-end">
                    <ButtonWithSpinner @click="changePassword" :loading="isLoading" text="Update"></ButtonWithSpinner>
                </div>
            </form>
        </div>
        <Modal :show="showSuccessModal" @closed="showSuccessModal = false" title="Password has been changed!">
        </Modal>
    </div>
</template>

<script>
    export default {
        components: {
        },

        props: [],

        data() {
            return {
                password: '',
                new_password: '',
                isLoading: false,
                errors: {},
                url: '/users/change-password/',
                showSuccessModal: false,
            }
        },

        mounted() {
        },

        methods: {

            changePassword() {
                this.isLoading = true
                this.errors = {}

                let payload = {
                    password: this.password,
                    new_password: this.new_password,
                }

                this.axios
                    .post(this.apiUrl + "users/change-password", payload)
                    .then(response => {
                        this.showSuccessModal = true
                        this.password = ""
                        this.new_password = ""
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