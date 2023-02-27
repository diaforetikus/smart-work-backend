<template>
    <div v-if="proposals.length || job.owner.id != store.user.id">
        <section aria-labelledby="notes-title">
            <div class="bg-white shadow sm:overflow-hidden sm:rounded-lg">
                <div class="divide-y divide-gray-200">
                    <div class="px-4 py-5 sm:px-6">
                        <h2 id="notes-title" class="text-lg font-medium text-gray-900">
                            <span v-if="job.owner.id === store.user.id">
                                <span v-if="job.executor">Executor</span>
                                <span v-else>Proposals</span>
                            </span>
                            <span v-else>My proposal</span>
                        </h2>
                    </div>
                    <div v-if="proposals.length" class="px-3 py-3">
                        <ProposalsList @createContract="createContract" :job="job" :proposals="proposals"></ProposalsList>
                    </div>
                </div>
                <div v-if="job.owner.id != store.user.id && !proposals.length" class="bg-gray-50 px-4 py-6 sm:px-6">
                    <AddProposalForm :job="job" @addedProposal="addedProposal"></AddProposalForm>
                </div>
            </div>
        </section>
        <Modal :show="showSuccessModal" @closed="showSuccessModal=false" title="Proposal has been added!">
        </Modal>
    </div>
</template>
<script>
import { userStore } from '../../../stores/user'
import ProposalsList from './ProposalsList.vue'
import AddProposalForm from './AddProposalForm.vue'

export default {
    components: {
        ProposalsList,
        AddProposalForm
    },

    props: ['job'],

    emits: ['createContract'],

    data() {
        return {
            store: userStore(),
            isLoading: false,

            proposals: [],

            proposal: {
                "text": "",
                "address": ""
            },

            errors: {},

            showSuccessModal: false,
        }
    },

    mounted() {
        this.getProposals()
    },

    methods: {

        getProposals()
        {
            let loader = this.$loading.show()

            this.axios
                .get(this.apiUrl + 'jobs/' + this.job.id + "/proposals")
                .then(response => {
                    this.proposals.push(...response.data)
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => {
                    loader.hide()
                })
        },

        addedProposal(proposal) {
            this.proposals.push(proposal)
        },

        createContract(proposal)
        {
            this.$emit("createContract", proposal)
        }
    }
}
</script>
