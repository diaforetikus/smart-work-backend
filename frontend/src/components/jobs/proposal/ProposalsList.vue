<template>
    <ul role="list" class="space-y-3">
        <li v-for="proposal in proposals" :key="proposal.id">
            <Proposal :proposal="proposal" :job="job" @createContract="createContract"></Proposal>
        </li>
    </ul>
</template>
<script>
import Proposal from './Proposal.vue'

export default {
    props: ['job', 'proposals'],

    emits: ["createContract"],

    components: {
        Proposal
    },

    methods: {
        createContract(proposal) {
            this.$emit("createContract", proposal)
        }
    }
}
</script>
