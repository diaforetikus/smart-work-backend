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
                                <div
                                    class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-yellow-100">
                                    <LinkIcon class="h-6 w-6 text-yellow-600" aria-hidden="true" />
                                </div>
                                <div class="mt-3 text-center sm:mt-5">
                                    <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">{{ title }}</DialogTitle>
                                    <div class="mt-2" v-if="text">
                                        <p class="text-sm text-gray-500">{{ text }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="mt-5 sm:mt-6 flex justify-between">
                                <button type="button" class="btn-primary mr-2" @click="yes">
                                    <span v-if="yes_text">{{ yes_text }}</span>
                                    <span v-else>No</span>
                                </button>
                                <button type="button" class="btn-secondary" @click="close">
                                    <span v-if="no_text">{{ no_text }}</span>
                                    <span v-else>No</span>
                                </button>
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
import { LinkIcon } from '@heroicons/vue/24/outline'


export default {

    props: ["show", "title", "text", "yes_text", "no_text"],

    components:
    {
        Dialog,
        DialogPanel,
        DialogTitle,
        TransitionChild,
        TransitionRoot,
        LinkIcon,
    },

    mounted() {
    },

    methods: {
        yes()
        {
            this.$emit("yes")
        },

        close()
        {
            this.$emit("no")
        }
    }
};
</script>
