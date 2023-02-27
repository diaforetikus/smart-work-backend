<template>
    <ButtonWithSpinner @click="cancel" :loading="isLoading" text="Cancel contract"></ButtonWithSpinner>
    <ConnectWalletModal :show="showConnectWalletModal" @closed="showConnectWalletModal=false"></ConnectWalletModal>
</template>

<script>
import { initializeConract, ERROR_CODE_TX_REJECTED_BY_USER } from '../smart-contract/utils'
import ConnectWalletModal from '../smart-contract/ConnectWalletModal.vue'

export default {
    components: { ConnectWalletModal },

    props: ['job'],

    emits: ['canceled'],

    data() {
        return {
            isLoading: false,
            showConnectWalletModal: false,
            startBlockNumber: null,
        }
    },

    async mounted() {
        /*
        this.loader = this.$loading.show()
        const contract = await initializeConract()
        const payment = await contract.getPaymentByJobId(this.job.id)
        this.loader.hide()

        if (payment.is_canceled && this.job.status == "waiting")
        {
            this.isLoading = true
            this.cancelProposal()
        }
        */
    },

    methods: {

        async cancel() {
            try {
                const signer = this.web3Provider.getSigner(0)
                const address = await signer.getAddress()
                this.startBlockNumber = await this.web3Provider.getBlockNumber()
                this.isLoading = true
                this.cancelPaymentInBlockchain()
            } catch (error) {
                console.log(error)
                console.log("Not connected")   
                this.showConnectWalletModal = true
            }
        },

        async cancelPaymentInBlockchain()
        {
            try {
                const smartWorkContract = await initializeConract()
                smartWorkContract.on('PaymentCanceled', (...args) => this.cancelPayment(args))

                const tx = await smartWorkContract.cancelPaymentByCient(parseInt(this.job.contract_id))

                await tx.wait()
            } catch(error) {
                if (error.code == ERROR_CODE_TX_REJECTED_BY_USER) 
                    return
                console.error(error)

                this.isLoading = false
            } finally {
                
            }
        },

        cancelPayment(args) {
            const blockNumber = args[1].blockNumber
            if (blockNumber <= this.startBlockNumber)
                return 

            this.cancelProposal()
        },

        cancelProposal() {
            this.axios
                .post(this.apiUrl + 'jobs/' + this.job.id + "/proposals/cancel")
                .then(response => {
                    this.$emit("canceled", response.data)
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => {
                    this.isLoading = false
                })
        },
    }
}
</script>
