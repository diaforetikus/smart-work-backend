<template>
    <div>
        <ButtonWithSpinner @click="accept" :loading="isLoading" text="Accept contract"></ButtonWithSpinner>
        <ConnectWalletModal :show="showConnectWalletModal" @closed="showConnectWalletModal=false"></ConnectWalletModal>
    </div>
</template>

<script>
import { initializeConract, ERROR_CODE_TX_REJECTED_BY_USER } from '../smart-contract/utils'
import ConnectWalletModal from '../smart-contract/ConnectWalletModal.vue'

export default {
    components: { ConnectWalletModal },

    props: ['job'],

    emits: ['accepted'],

    data() {
        return {
            isLoading: false,
            showConnectWalletModal: false,
            startBlockNumber: null,
        }
    },

    async mounted() {
        this.loader = this.$loading.show()
        try {
            
            const contract = await initializeConract()
            const payment = await contract.getPaymentById(this.job.contract_id)
            this.loader.hide()
            if (payment.is_accepted && this.job.status == "waiting")
            {
                this.isLoading = true
                this.acceptJob()
            }
        } catch (error) {
            this.loader.hide()
            console.log(error)
            console.log("Not connected")   
        }
    },

    methods: {

        async accept() 
        {
            try {
                const signer = this.web3Provider.getSigner(0)
                const address = await signer.getAddress()
                this.startBlockNumber = await this.web3Provider.getBlockNumber()
                this.isLoading = true
                this.acceptPaymentInBlockchain()
            } catch (error) {
                console.log(error)
                console.log("Not connected")   
                this.showConnectWalletModal = true
            }
        },

        async acceptPaymentInBlockchain()
        {
            try {
                const smartWorkContract = await initializeConract()
                smartWorkContract.on('PaymentAccepted', (...args) => this.acceptPayment(args))

                const tx = await smartWorkContract.acceptPayment(parseInt(this.job.contract_id))

                await tx.wait()
            } catch(error) {
                if (error.code == ERROR_CODE_TX_REJECTED_BY_USER) 
                    return
                console.error(error)
                this.isLoading = false
            } finally {
                
            }
        },

        acceptPayment(args) {
            const blockNumber = args[1].blockNumber
            if (blockNumber <= this.startBlockNumber)
                return 

            this.acceptJob()
        },

        acceptJob() {
            this.axios
                .post(this.apiUrl + 'jobs/' + this.job.id + "/accept")
                .then(response => {
                    this.$emit("accepted", response.data)
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => {
                    this.isLoading = false
                })
        }
    }
}
</script>
