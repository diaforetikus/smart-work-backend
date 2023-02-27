<template>
    <div class="flex space-x-3">
        <div class="flex-shrink-0">
            <img class="h-10 w-10 rounded-full" :src="icon" alt="">
        </div>
        <div class="min-w-0 flex-1">
            <form @submit.prevent="addProposal" class="space-y-4">
                <div>
                    <label for="text" class="sr-only">Your proposal</label>
                    <textarea v-model="proposal.text" :class="'field ' + (errors.text ? 'field-error' : '')" id="text" rows="5" placeholder="Proposal text"></textarea>
                    <div v-if="errors.text" class="text-sm mt-1 text-red-600">{{ errors.text }}</div>
                </div>
                <div>
                    <label for="address" class="sr-only">Wallet address</label>
                    <input v-model="proposal.address" :class="'field ' + (errors.address ? 'field-error' : '')" id="address" type="text" placeholder="Wallet address"/>
                    <div v-if="errors.address" class="text-sm mt-1 text-red-600">{{ errors.address }}</div>
                </div>
                <div class="flex items-center justify-end">
                    <div>
                        <ButtonWithSpinner :loading="isLoading" text="Add proposal"></ButtonWithSpinner>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <Modal :show="showSuccessModal" @closed="showSuccessModal=false" title="Proposal has been added!">
    </Modal>
</template>
<script>
import { userStore } from '../../../stores/user'


export default {
    props: ['job'],

    components: {
        
    },

    emits: ['addedProposal'],

    computed: {
        icon: {
            get() {
                let idStr = this.store.user.id.toString()
                if (idStr.length === 1)
                    idStr = '00' + idStr
                else if  (idStr.length === 2)
                    idStr = '0' + idStr

                return '/assets/cryptopunks-icons/punk' + idStr + '.png'
            },
        }
    },

    data() {
        return {
            store: userStore(),
            isLoading: false,

            proposal: {
                "text": "",
                "address": ""
            },

            errors: {},

            showSuccessModal: false,
        }
    },

    mounted() {
        
    },

    methods: {
        addProposal() {
            this.errors = {}
            this.isLoading = true

            this.axios
                .post(this.apiUrl + 'jobs/' + this.job.id + "/proposals", this.proposal)
                .then(response => {
                    this.$emit("addedProposal", response.data)
                    this.showSuccessModal = true
                    this.proposal.text = ""
                    this.proposal.address = ""
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
        }
    }
}
</script>
