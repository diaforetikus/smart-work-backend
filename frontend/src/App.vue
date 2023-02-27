<template>
    <div class="min-h-full bg-gray-50">
        <div>
            <Disclosure as="nav" class="bg-gradient-to-r from-slate-900 via-zinc-800 to-slate-900" v-slot="{ open }">
                <div class="mx-auto max-w-7xl sm:px-6 lg:px-8" id="header">
                    <div>
                        <div class="flex h-16 items-center justify-between px-4 sm:px-0">
                            <div class="flex items-center">
                                <div class="flex-shrink-0">
                                    <RouterLink to="/"><img class="h-8 w-8"
                                            src="https://tailwindui.com/img/logos/mark.svg?color=lime&shade=500"
                                            alt="Your Company" /></RouterLink>
                                </div>
                                <div class="hidden md:block">
                                    <div class="flex items-baseline space-x-4">
                                        <TopMenu></TopMenu>
                                    </div>
                                </div>
                            </div>
                            <div class="hidden md:block">
                                <ProfileMenu></ProfileMenu>
                            </div>
                            <div class="-mr-2 flex md:hidden">
                                <!-- Mobile menu button -->
                                <DisclosureButton
                                    class="inline-flex items-center justify-center rounded-md bg-gray-800 p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                                    <span class="sr-only">Open main menu</span>
                                    <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
                                    <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
                                </DisclosureButton>
                            </div>
                        </div>
                    </div>
                </div>
                <DisclosurePanel class="border-b border-gray-700 md:hidden">
                    <div class="space-y-1 px-2 py-3 sm:px-3">
                        <DisclosureButton v-for="item in navigation" :key="item.name" as="a" :href="item.href"
                            :class="[item.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'block px-3 py-2 rounded-md text-base font-medium']"
                            :aria-current="item.current ? 'page' : undefined">{{ item.name }}</DisclosureButton>
                    </div>
                    <div class="border-t border-gray-700 pt-4 pb-3">
                        <div class="flex items-center px-5">
                            <div class="flex-shrink-0">
                                <img class="h-10 w-10 rounded-full" :src="user.imageUrl" alt="" />
                            </div>
                            <div class="ml-3">
                                <div class="text-base font-medium leading-none text-white">{{ user.name }}</div>
                                <div class="text-sm font-medium leading-none text-gray-400">{{ user.email }}</div>
                            </div>
                            <button type="button"
                                class="ml-auto flex-shrink-0 rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                                <span class="sr-only">View notifications</span>
                                <BellIcon class="h-6 w-6" aria-hidden="true" />
                            </button>
                        </div>
                        <div class="mt-3 space-y-1 px-2">
                            <DisclosureButton v-for="item in userNavigation" :key="item.name" as="a" :href="item.href"
                                class="block rounded-md px-3 py-2 text-base font-medium text-gray-400 hover:bg-gray-700 hover:text-white">
                                {{ item.name }}</DisclosureButton>
                        </div>
                    </div>
                </DisclosurePanel>
            </Disclosure>
        </div>
        <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8 py-10">
            <RouterView />
        </div>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline'
import ProfileMenu from './components/ProfileMenu.vue'
import TopMenu from './components/TopMenu.vue'
import { userStore } from './stores/user'

const navigation = [
    { name: 'Home', href: '/', current: true },
    { name: 'About', href: '/about', current: false },
]

const user = JSON.parse(localStorage.getItem('user'));
if (user && user.token)
    userStore().setUser(user)


</script>
