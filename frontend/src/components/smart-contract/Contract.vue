<script>
import { useStore } from '../../stores/blockchain.js'
import { ethers } from 'ethers'
import smartWorkAddress from '../../../contracts/SmartWork-contract-address'
import smartArtifact from '../../../contracts/SmartWork.json'

export default {
    
    setup() {

        const store = useStore()

        const mountWalletAndContract = async () =>
        {
            const smartWorkContract = await initializeConract(this.web3Provider)

            store.setAccount((await connectWallet()))
            store.setBalance((await getBalance(store.account)))
            store.setSmartWorkContract(null)

            return smartWorkContract
        }

        const connectWallet = async () =>
        {
            if (!checkMetamask())
                return

            if (!checkNetwork())
                return

            const [selectedAddress] = await ethereum.request({
                method: 'eth_requestAccounts'
            })
            
            ethereum.on('accountsChanged', async ([newAddress]) => {
                this.store.setAccount(newAddress)
                this.store.setBalance((await getBalance(this.selectedAddress)))
                this.store.smartWorkContract((await initializeConract(this.web3Provider)))
            })

            ethereum.on('chainChanged', ([networkId]) => {
                this.store.setAccount(null)
                this.store.setBalance(0)
                this.store.smartWorkContract(null)
            })

            return selectedAddress
        }

        const initializeConract = async () =>
        {
            
            const smartWorkContract = new ethers.Contract(
                smartWorkAddress.SmartWork,
                smartArtifact.abi,
                this.web3Provider.getSigner(0)
            )

            return smartWorkContract
        }

        const getBalance = async (selectedAddress) => 
        {
            const balance = await this.web3Provider.getBalance(selectedAddress)
            return ethers.utils.formatEther(balance.toString())
        }

        const checkMetamask = () =>
        {
            if (window.ethereum === undefined)
            {
                this.networkError = "Please install Metamask"
                return false
            }

            return true
        }

        const checkNetwork = () => {

            if (window.ethereum.networkVersion === HARDHAT_NETWORK_ID)
                return true

            this.networkError = "Please connect to localhost:8545"
            return false
        }
    }
}
</script>