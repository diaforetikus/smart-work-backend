
<template>
    <TransitionRoot as="template" :show="show">
        <Dialog as="div" class="relative z-10" @close="close">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 overflow-y-auto">
                <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
                            <div>
                                <div class="flex justify-center">
                                    <img src="/assets/metamask.svg" class="w-28" />
                                </div>
                                <div class="mt-3 text-center sm:mt-5">
                                    <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">Do you want to connect wallet?</DialogTitle>
                                    <div class="mt-2">
                                        <p class="text-sm text-gray-500"></p>
                                    </div>
                                </div>
                            </div>
                            <div class="mt-5 sm:mt-6 flex justify-between">
                                <button @click="connectWallet" type="button" class="btn-primary mr-2">Connect wallet</button>
                                <button type="button" class="btn-gray" @click="close">Close</button>
                            </div>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
</template>

<script>

    import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
    import { CheckIcon } from '@heroicons/vue/24/outline'
    import { mountWalletAndContract } from './utils'

    export default {

        components:
        {
            Dialog,
            DialogPanel,
            DialogTitle,
            TransitionChild,
            TransitionRoot,
            CheckIcon,
        },

        emits: ["closed"],

        setup({show}, {emit}) {

            const connectWallet = () => {
                mountWalletAndContract()
                emit("closed")
            }

            const close = () =>  {
                emit("closed")
            }

            return { connectWallet, close, show }
        }
    }
</script>
