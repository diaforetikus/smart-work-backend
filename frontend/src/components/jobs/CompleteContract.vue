<template>
    <ButtonWithSpinner @click="complete" :loading="isLoading" text="Complete contract"></ButtonWithSpinner>
    <ConnectWalletModal :show="showConnectWalletModal" @closed="showConnectWalletModal=false"></ConnectWalletModal>
</template>

<script>
import { initializeConract, ERROR_CODE_TX_REJECTED_BY_USER } from '../smart-contract/utils'
import ConnectWalletModal from '../smart-contract/ConnectWalletModal.vue'

export default {
    components: { ConnectWalletModal },

    props: ['job'],

    emits: ['completed'],

    data() {
        return {
            isLoading: false,
            showConnectWalletModal: false,
            startBlockNumber: null
        }
    },

    async mounted() {
        this.loader = this.$loading.show()
        try {
            
            const contract = await initializeConract()
            const payment = await contract.getPaymentById(this.job.contract_id)
            this.loader.hide()

            if (payment.is_paid && this.job.status == "at work")
            {
                this.isLoading = true
                this.completeJob()
            }
        } catch (error) {
            this.loader.hide()
            console.log(error)
            console.log("Not connected")   
        }
    },

    methods: {
        async complete() 
        {
            try {
                const signer = this.web3Provider.getSigner(0)
                const address = await signer.getAddress()
                this.startBlockNumber = await this.web3Provider.getBlockNumber()
                this.isLoading = true
                this.completePaymentInBlockchain()
            } catch (error) {
                console.log(error)
                console.log("Not connected")   
                this.showConnectWalletModal = true
            }
        },

        async completePaymentInBlockchain()
        {
            try {
                const smartWorkContract = await initializeConract()
                smartWorkContract.on('PaymentSend', (...args) => this.completePayment(args))

                const tx = await smartWorkContract.sendPayment(parseInt(this.job.contract_id))

                await tx.wait()
            } catch(error) {
                if (error.code == ERROR_CODE_TX_REJECTED_BY_USER) 
                    return
                console.error(error)
                this.isLoading = false
            } finally {
                
            }
        },

        completePayment(args) {
            const blockNumber = args[1].blockNumber
            if (blockNumber <= this.startBlockNumber)
                return 

            this.completeJob()
        },

        completeJob() {
            this.axios
                .post(this.apiUrl + 'jobs/' + this.job.id + "/complete")
                .then(response => {
                    this.$emit("completed", response.data)
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
