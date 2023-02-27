<template>
    <div v-if="job.status === 'open' || (job.status != 'open' && proposal.status === 'accepted') ">
        <div :class="'sm:rounded-lg border-transparent border-2 px-2 py-2 ' + (job.status === 'open' ? 'hover:border-green-500' : '')">
            <div class="flex justify-between">
                <div class="flex items-center">
                    <img class="h-9 w-9 rounded-full mr-2 bg-lime-300 border-2 border-gray-800" :src="icon" alt="">
                    <div class="text-sm">
                        <a href="#" class="font-medium text-gray-900">{{ proposal.user.first_name + " " + proposal.user.last_name }}</a>
                    </div>
                </div>
                <div>
                    <div class="text-sm font-medium text-gray-500"><time :datetime="moment(proposal.created_at).format('MMM Do YYYY, h:mm')">{{ moment(proposal.created_at).format("MMM Do YYYY, h:mm") }}</time></div>
                    <div v-if="job.status === 'open'" class="flex justify-end mt-1">
                        <button v-if="store.user.id === job.owner.id" @click="createContract" type="button" class="btn-small">Sign contract</button>
                    </div>
                </div>
            </div>
            <div class="mt-1 text-sm text-gray-700">
                {{ proposal.text }}
            </div>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
import { userStore } from '../../../stores/user'


export default {

    components: {
    },

    props: ['job', 'proposal'],

    emits: ['createContract'],

    data() {
        return {
            store: userStore(),
            moment: moment,
            showModal: false,
            showSuccessModal: false,
            showConnectWalletModal: false,
            contractID: null,
            startBlockNumber: null,
            loader: null
        }
    },

    computed: {
        icon: {
            get() {
                let idStr = this.proposal.user.id.toString()
                if (idStr.length === 1)
                    idStr = '00' + idStr
                else if  (idStr.length === 2)
                    idStr = '0' + idStr

                return '/assets/cryptopunks-icons/punk' + idStr + '.png'
            },
        }
    },

    async mounted() {
    },

    methods: {

       async createContract()
       {
            this.$emit("createContract", this.proposal)
       },
    }
}
</script>