<template>
    <div>
        <div class="bg-white px-6 pt-6 pb-6 shadow rounded-lg">
            <form class="space-y-4">
                <div>
                    <label for="first_name" class="label">
                        First name
                    </label>
                    <div class="mt-1">
                        <input v-model="user.first_name" @change="errors.first_name = null" id="first_name" name="first_name" type="text"
                            :class="'field ' + (errors.first_name ? 'field-error' : '')">
                    </div>
                    <p v-if="errors.first_name" class="mt-2 text-sm text-red-600">{{ errors.first_name }}</p>
                </div>

                <div>
                    <label for="last_name" class="label">
                        Last name
                    </label>
                    <div class="mt-1">
                        <input v-model="user.last_name" @change="errors.last_name = null" id="last_name" name="last_name" type="text"
                            :class="'field ' + (errors.last_name ? 'field-error' : '')">
                    </div>
                    <p v-if="errors.last_name" class="mt-2 text-sm text-red-600">{{ errors.last_name }}</p>
                </div>
                <div class="flex justify-end">
                    <ButtonWithSpinner @click="updateProfile" :loading="isLoading" text="Update"></ButtonWithSpinner>
                </div>
            </form>
        </div>

        <Modal :show="showSuccessModal" @closed="showSuccessModal = false" title="Your bio have been updated!">
        </Modal>
    </div>
</template>

<script>

import { userStore } from '../../stores/user'


export default {
    props: [],

    data() {
        return {
            menu: '',
            user: userStore().user,
            isLoading: false,
            errors: {},
            url: '/api/users/',
            showSuccessModal: false,
        }
    },

    mounted() {

    },

    methods: {
        updateProfile() {
            this.isLoading = true
            this.errors = {}

            const payload = {
                "first_name": this.user.first_name,
                "last_name": this.user.last_name,
            }

            this.axios
                .patch(this.apiUrl + 'users/update-bio', payload)
                .then(response => {
                    this.showSuccessModal = true
                    localStorage.setItem('user', JSON.stringify(this.user));
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