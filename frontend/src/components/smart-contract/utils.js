import { ethers } from 'ethers'
import smartWorkAddress from '../../../contracts/SmartWork-contract-address'
import smartArtifact from '../../../contracts/SmartWork.json'

import usdtAddress from '../../../contracts/Usdt-contract-address.json'
import usdtAddressMumbai from '../../../contracts/Usdt-contract-address-mumbai.json'
import usdtArtifact from '../../../contracts/Usdt.json'

import { userStore } from '../../stores/user.js'

export const HARDHAT_NETWORK_ID = '31337'
export const MUMBAI_NETWORK_ID = '80001'
export const ERROR_CODE_TX_REJECTED_BY_USER = 4001
const web3Provider = new ethers.providers.Web3Provider(window.ethereum)
const store = userStore()

let networkError = false
let smartWorkContract = null

const mountWalletAndContract = async () =>
{
    const address = await connectWallet()
    smartWorkContract = await initializeConract()

    store.user.account = address
    store.user.balance = await getBalance(address)

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
        store.user.account = newAddress
        store.user.balance = await getBalance(newAddress)
    })

    ethereum.on('chainChanged', ([networkId]) => {
        store.user.account = null
        store.user.balance = 0
    })

    return selectedAddress
}

const initializeConract = async () =>
{   
    const smartWorkContract = new ethers.Contract(
        smartWorkAddress.SmartWork,
        smartArtifact.abi,
        web3Provider.getSigner(0)
    )

    return smartWorkContract
}

const initializeUsdtToken = async () =>
{   
    let usdAddress = usdtAddress.Usdt

    if (window.ethereum.networkVersion === MUMBAI_NETWORK_ID)
        usdAddress = usdtAddressMumbai.Usdt

    const smartWorkContract = new ethers.Contract(
        usdAddress,
        usdtArtifact.abi,
        web3Provider.getSigner(0)
    )

    return smartWorkContract
}

const getBalance = async (selectedAddress) => 
{
    const balance = await web3Provider.getBalance(selectedAddress)
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

    console.log(window.ethereum.networkVersion)

    if (window.ethereum.networkVersion === HARDHAT_NETWORK_ID || window.ethereum.networkVersion === MUMBAI_NETWORK_ID)
        return true

    console.log("Please connect to localhost:8545")
    return false
}

export { mountWalletAndContract, initializeConract, initializeUsdtToken, getBalance }