<template>
    <div class="py-10">
        <main v-if="job">
            <!-- Page header -->
            <div
                class="mx-auto max-w-3xl md:flex md:items-center md:justify-between md:space-x-5 lg:max-w-7xl">
                <div class="flex items-center space-x-5">
                    <div class="flex-shrink-0">
                        <div class="relative">
                            <img class="h-16 w-16 bg-gradient-to-r from-purple-500 via-orange-500 to-purple-500 rounded-full block border-2 border-gray-800" :src="icon" alt="">
                            <span class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true"></span>
                        </div>
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold text-gray-900">{{ job.owner.first_name + " " + job.owner.last_name }}</h1>
                        <p class="text-sm font-medium text-gray-500">Posted job in category <a href="#" class="text-gray-900">{{ job.category.name }}</a> on <time :datetime="moment(job.created_at).format('MMMM Do YYYY, h:mm')">{{ moment(job.created_at).format("MMMM Do YYYY, h:mm") }}</time></p>
                    </div>
                </div>
                <div>
                    <span v-if="job.status != 'open'" :class="'inline-flex items-center rounded-full text-xl px-4 py-2 font-medium mt-2 ' + getBadgeColor(job.status)">{{ job.status }}</span>
                </div>
            </div>

            <div
                class="mx-auto mt-8 grid max-w-3xl grid-cols-1 gap-6 lg:max-w-7xl lg:grid-flow-col-dense lg:grid-cols-3">
                <div class="space-y-6 lg:col-span-2 lg:col-start-1">
                    <!-- Description list-->
                    <section aria-labelledby="applicant-information-title">
                        <div class="bg-white shadow sm:rounded-lg">
                            <div class="px-4 py-5 sm:px-6">
                                <h2 id="applicant-information-title" class="text-lg font-medium leading-6 text-gray-900">
                                    {{ job.title }}</h2>
                            </div>
                            <div class="border-t border-gray-200 px-4 py-5 sm:px-6">
                                <dl class="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2">
                                    <div class="sm:col-span-1">
                                        <dt class="text-sm font-medium text-gray-500">Job category</dt>
                                        <dd class="mt-1 text-sm text-gray-900">{{ job.category.name }}</dd>
                                    </div>
                                    <div class="sm:col-span-1">
                                        <dt class="text-sm font-medium text-gray-500">Salary expectation</dt>
                                        <div class="flex items-center">
                                            <img src="/assets/tether.svg" class="w-5 h-5 mr-1 mt-0.5 block" />
                                            <dd class="mt-1 text-sm text-gray-900 font-medium">${{ job.amount }}</dd>
                                        </div>
                                    </div>
                                    <div class="sm:col-span-2">
                                        <dt class="text-sm font-medium text-gray-500">About</dt>
                                        <dd class="mt-1 text-sm text-gray-900">{{ job.description }}</dd>
                                    </div>
                                </dl>
                            </div>
                        </div>
                    </section>

                    <!-- Proposals-->
                    <Proposals :job="job" @createContract="createContract"></Proposals>
                </div>

                <section aria-labelledby="timeline-title" class="lg:col-span-1 lg:col-start-3">
                    <div class="bg-white px-4 py-5 shadow sm:rounded-lg sm:px-6">
                        <h2 id="timeline-title" class="text-lg font-medium text-gray-900">Timeline</h2>

                        <!-- Activity Feed -->
                        <div class="mt-6 flow-root">
                            <ul role="list" class="-mb-8">
                                <li>
                                    <div class="relative pb-8">
                                        <span v-if="job.status != 'open'" class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                                            aria-hidden="true"></span>
                                        <div class="relative flex space-x-3">
                                            <div>
                                                <span
                                                    class="h-8 w-8 rounded-full bg-gradient-to-r from-neutral-500 via-slate-600 to-neutral-500 flex items-center justify-center ring-8 ring-white">
                                                    <!-- Heroicon name: mini/user -->
                                                    <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg"
                                                        viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                        <path
                                                            d="M10 8a3 3 0 100-6 3 3 0 000 6zM3.465 14.493a1.23 1.23 0 00.41 1.412A9.957 9.957 0 0010 18c2.31 0 4.438-.784 6.131-2.1.43-.333.604-.903.408-1.41a7.002 7.002 0 00-13.074.003z" />
                                                    </svg>
                                                </span>
                                            </div>
                                            <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                                <div>
                                                    <p class="text-sm text-gray-500">Posted job by <a href="#"
                                                            class="font-medium text-gray-900">{{ job.owner.first_name + " " + job.owner.last_name }}</a></p>
                                                </div>
                                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                                    <time datetime="2020-09-20">{{ moment(job.created_at).format("MMM D, h:mm") }}</time>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>

                                <li v-if="['waiting', 'at work', 'completed'].includes(job.status)">
                                    <div class="relative pb-8">
                                        <span v-if="['at work', 'completed'].includes(job.status)" class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                                            aria-hidden="true"></span>
                                        <div class="relative flex space-x-3">
                                            <div>
                                                <span
                                                    class="h-8 w-8 rounded-full bg-gradient-to-r from-yellow-500 via-orange-400 to-yellow-500 flex items-center justify-center ring-8 ring-white">
                                                    <!-- Heroicon name: mini/hand-thumb-up -->
                                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-white">
                                                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                                    </svg>
                                                </span>
                                            </div>
                                            <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                                <div>
                                                    <p class="text-sm text-gray-500">Waiting accepting from <a
                                                            href="#" class="font-medium text-gray-900">{{ job.executor.first_name + " " + job.executor.last_name }}</a></p>
                                                </div>
                                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                                    <time :datetime="moment(job.assigned_at).format('MMM D, h:mm')">{{ moment(job.assigned_at).format("MMM D, h:mm") }}</time>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>

                                <li v-if="['at work', 'completed'].includes(job.status)">
                                    <div class="relative pb-8">
                                        <span v-if="job.status === 'completed'" class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                                            aria-hidden="true"></span>
                                        <div class="relative flex space-x-3">
                                            <div>
                                                <span
                                                    class="h-8 w-8 rounded-full bg-gradient-to-r from-cyan-500 via-blue-400 to-cyan-500 flex items-center justify-center ring-8 ring-white">
                                                    <!-- Heroicon name: mini/hand-thumb-up -->
                                                    <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg"
                                                        viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                        <path
                                                            d="M1 8.25a1.25 1.25 0 112.5 0v7.5a1.25 1.25 0 11-2.5 0v-7.5zM11 3V1.7c0-.268.14-.526.395-.607A2 2 0 0114 3c0 .995-.182 1.948-.514 2.826-.204.54.166 1.174.744 1.174h2.52c1.243 0 2.261 1.01 2.146 2.247a23.864 23.864 0 01-1.341 5.974C17.153 16.323 16.072 17 14.9 17h-3.192a3 3 0 01-1.341-.317l-2.734-1.366A3 3 0 006.292 15H5V8h.963c.685 0 1.258-.483 1.612-1.068a4.011 4.011 0 012.166-1.73c.432-.143.853-.386 1.011-.814.16-.432.248-.9.248-1.388z" />
                                                    </svg>
                                                </span>
                                            </div>
                                            <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                                <div>
                                                    <p class="text-sm text-gray-500">Accepted job by <a
                                                            href="#" class="font-medium text-gray-900">{{ job.executor.first_name + " " + job.executor.last_name }}</a></p>
                                                </div>
                                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                                    <time :datetime="moment(job.started_at).format('MMM D, h:mm')">{{ moment(job.started_at).format("MMM D, h:mm") }}</time>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>

                                <li v-if="job.status === 'completed'">
                                    <div class="relative pb-8">
                                        <div class="relative flex space-x-3">
                                            <div>
                                                <span
                                                    class="h-8 w-8 rounded-full bg-gradient-to-r from-lime-500 via-green-500 to-lime-500 flex items-center justify-center ring-8 ring-white">
                                                    <!-- Heroicon name: mini/check -->
                                                    <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg"
                                                        viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                        <path fill-rule="evenodd"
                                                            d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z"
                                                            clip-rule="evenodd" />
                                                    </svg>
                                                </span>
                                            </div>
                                            <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                                <div>
                                                    <p class="text-sm text-gray-500">Completed contract with <a href="#"
                                                            class="font-medium text-gray-900">{{ job.executor.first_name + " " + job.executor.last_name }}</a></p>
                                                </div>
                                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                                    <time :datetime="moment(job.completed_at).format('MMM D, h:mm')">{{ moment(job.completed_at).format("MMM D, h:mm") }}</time>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>

                                <li v-if="job.status === 'canceled'">
                                    <div class="relative pb-8">
                                        <div class="relative flex space-x-3">
                                            <div>
                                                <span
                                                    class="h-8 w-8 rounded-full bg-gradient-to-r from-orange-500 via-red-500 to-orange-500 flex items-center justify-center ring-8 ring-white">
                                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-white">
                                                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                                                    </svg>
                                                </span>
                                            </div>
                                            <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                                                <div>
                                                    <p class="text-sm text-gray-500">Canceled contract by <a href="#"
                                                            class="font-medium text-gray-900">{{ job.owner.first_name + " " + job.owner.last_name }}</a></p>
                                                </div>
                                                <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                                    <time :datetime="moment(job.updated_at).format('MMM D, h:mm')">{{ moment(job.updated_at).format("MMM D, h:mm") }}</time>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div v-if="job.status === 'waiting' && job.executor.id === store.user.id" class="-mt-4">
                        <div class="mt-10">
                            <AcceptContract :job="job" @accepted="acceptedContract"></AcceptContract>
                        </div>
                    </div>
                    <div v-if="job.status === 'at work' && job.owner.id === store.user.id" class="-mt-4">
                        <div class="mt-10">
                            <CompleteContract :job="job" @completed="completedContract"></CompleteContract>
                        </div>
                    </div>
                    <div v-if="job.status === 'waiting' && job.owner.id === store.user.id" class="-mt-4">
                        <div class="mt-10">
                            <CancelContract :job="job" @canceled="canceledContract"></CancelContract>
                        </div>
                    </div>
                </section>
            </div>
        </main>
        
        <Teleport to="body">
            <Modal v-if="job" :show="showSuccessModal" @closed="closed" :title="successTitle">
            </Modal>
            <ConnectWalletModal :show="showConnectWalletModal" @closed="showConnectWalletModal=false"></ConnectWalletModal>
        </Teleport>
    </div>
</template>

<script>
import moment from 'moment'
import { ethers } from 'ethers'
import { userStore } from '../../stores/user'
import Proposals from '../../components/jobs/proposal/Proposals.vue'
import AcceptContract from '../../components/jobs/AcceptContract.vue'
import CompleteContract from '../../components/jobs/CompleteContract.vue'
import CancelContract from '../../components/jobs/CancelContract.vue'
import { getBadgeColor } from '../../utils'
import ConnectWalletModal from '../../components/smart-contract/ConnectWalletModal.vue'
import { initializeConract, initializeUsdtToken, ERROR_CODE_TX_REJECTED_BY_USER } from '../../components/smart-contract/utils'


export default {
    components: {
        Proposals,
        AcceptContract,
        CompleteContract,
        CancelContract,
        ConnectWalletModal,
    },

    data() {
        return {
            job: null,
            moment: moment,
            store: userStore(),
            isLoading: false,
            showAcceptModal: false,
            showSuccessModal: false,
            showCompleteModal: false,
            showConnectWalletModal: false,
            getBadgeColor: getBadgeColor,
            successTitle: '',
            proposal: null,
        }
    },

    computed: {
        icon: {
            get() {
                let idStr = this.job.owner.id.toString()
                if (idStr.length === 1)
                    idStr = '00' + idStr
                else if  (idStr.length === 2)
                    idStr = '0' + idStr

                return '/assets/cryptopunks-icons/punk' + idStr + '.png'
            },
        }
    },

    async mounted() {
        await this.getJob()

        if (this.job.status != "open")
            return
        
        this.loader = this.$loading.show()
        try {
            const contract = await initializeConract()
            const payment = await contract.getPaymentByJobId(this.job.id)
            this.loader.hide()
            if (payment.id > 0 && payment.proposal_id > 0)
            {
                this.loader = this.$loading.show()
                this.signContract(payment.id.toNumber(), payment.proposal_id.toNumber())
            }
        } catch (error) {
            this.loader.hide()
            console.log(error)
            console.log("Not connected")   
        }
    },

    methods: {
        async getJob() {
            let loader = this.$loading.show()

            await this.axios
                .get(this.apiUrl + 'jobs/' + this.$route.params.id)
                .then(response => {
                    this.job = response.data
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => {
                    loader.hide()
                })
        },

        acceptedContract(data)
        {
            this.job = data
            this.showSuccessModal = true
            this.successTitle = "Contract accepted!"
        },

        completedContract(data)
        {
            this.job = data
            this.showSuccessModal = true
            this.successTitle = "Contract completed!"
        },

        canceledContract(data) 
        {
            this.job = data
            this.showSuccessModal = true
            this.successTitle = "Contract canceled!"
        },

        async createContract(proposal)
        {
            this.proposal = proposal

            try {
                const signer = this.web3Provider.getSigner(0)
                const address = await signer.getAddress()
                this.startBlockNumber = await this.web3Provider.getBlockNumber()
                this.createPaymentInBlockchain()
            } catch (error) {
                console.log(error)
                console.log("Not connected")   
                this.showConnectWalletModal = true
            }
        },

        async createPaymentInBlockchain()
        {
            this.loader = this.$loading.show()

            try {

                const smartWorkContract = await initializeConract()
                const usdtToken = await initializeUsdtToken()

                const amount = ethers.utils.parseUnits(this.job.amount.toString(), 6)

                console.log(usdtToken.address)
                console.log(smartWorkContract.address)
                console.log(amount)

                const approval = await usdtToken.approve(smartWorkContract.address, amount)
                await approval.wait()

                smartWorkContract.on('PaymentCreated', (...args) => this.paymentCreated(args))

                const tx = await smartWorkContract.createPayment(
                    this.proposal.address, 
                    amount,
                    this.job.id,
                    this.proposal.id
                )

                await tx.wait()
            } catch(error) {
                console.log(error)
                if (error.code == ERROR_CODE_TX_REJECTED_BY_USER) 
                    return

                this.loader.hide()
            } finally {
                
            }
        },

        async paymentCreated(args) {
            const blockNumber = args[1].blockNumber

            if (blockNumber <= this.startBlockNumber)
                return 

            this.signContract(args[0].toString(), this.proposal.id)
        },

        signContract(contractId, proposalId) {
            this.showModal = false

            const payload = {
                "contract_id": contractId
            }

            this.axios
                .post(this.apiUrl + 'jobs/' + this.job.id + "/proposals/accept/" + proposalId, payload)
                .then(response => {
                    /*
                    this.proposal.status_id = response.data.status_id
                    this.proposal.status = response.data.status

                    this.job.status_id = 2
                    this.job.status = "waiting"
                    this.job.executor = response.data.user
                    this.job.assigned_at = response.data.created_at
                    */

                    if (!this.proposal)
                        this.proposal = {"id": proposalId}

                    this.showSuccessModal = true
                    this.successTitle = "Contract signed!"
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => {
                    this.loader.hide()
                })
        },

        closed() {
            this.showSuccessModal=false
            
            if (this.proposal)
                window.location.reload()
        }
    }
}
</script>
