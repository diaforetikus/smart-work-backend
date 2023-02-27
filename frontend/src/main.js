import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from "axios"
import { ethers } from 'ethers'
import './assets/main.css'

/**
 * Pinia
 */
import { createPinia } from 'pinia'
const app = createApp(App)
app.use(createPinia())

/**
 * Vue loading overlay
 */
import {LoadingPlugin} from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css'
app.use(LoadingPlugin)

app.config.globalProperties.axios = axios

let apiUrl = new URL('/api/', window.location).href
if (window.location.hostname == "127.0.0.1" || window.location.hostname == "localhost")
    apiUrl = "http://127.0.0.1:8000/api/"

app.config.globalProperties.apiUrl = apiUrl

//app.config.globalProperties.user = null

const user = JSON.parse(localStorage.getItem('user'));
if (user && user.token) {
    app.config.globalProperties.axios.defaults.headers.common['Authorization'] = `Bearer ${user.token}`;
    //app.config.globalProperties.user = user
}

app.use(router)

//localStorage.removeItem('user');

/**
 * Web3Provider
 */
//app.config.unwrapInjectedRef = true 
app.config.globalProperties.web3Provider = new ethers.providers.Web3Provider(window.ethereum)


/**
 * Components
 */

import ButtonWithSpinner from "./components/buttons/ButtonWithSpinner.vue"
app.component("ButtonWithSpinner", ButtonWithSpinner);

/**
 * Modals
 */
import Modal from "./components/Modal.vue"
app.component("Modal", Modal);

import ModalYesNo from "./components/ModalYesNo.vue"
app.component("ModalYesNo", ModalYesNo);


app.mount('#app')
