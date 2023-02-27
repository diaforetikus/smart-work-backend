<template>
    <div v-if="!store.user" class="hidden md:flex md:items-center md:space-x-6">
        <RouterLink to="/signin"
            :class="($router.currentRoute.value.path === '/signin' ? 'inline-flex items-center rounded-md border border-transparent bg-gray-600 px-4 py-2 text-base font-medium text-white hover:bg-gray-700' : 'text-base font-medium text-white hover:text-gray-300')">
            Sign In</RouterLink>
        <RouterLink to="/signup"
            :class="($router.currentRoute.value.path === '/signup' ? 'inline-flex items-center rounded-md border border-transparent bg-gray-600 px-4 py-2 text-base font-medium text-white hover:bg-gray-700' : 'text-base font-medium text-white hover:text-gray-300')">
            Sign Up</RouterLink>
    </div>
    <div v-else class="ml-4 flex items-center md:ml-6">
        <Menu as="div" class="relative ml-3">
            <div>
                <MenuButton
                    class="flex max-w-xs items-center rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                    <span class="sr-only">Open user menu</span>
                    <img class="h-8 w-8 rounded-full block border border-gray-300" :src="icon" alt="" />
                </MenuButton>
            </div>

            <transition enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95">
                <MenuItems
                    class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <MenuItem v-slot="{ active }">
                        <RouterLink to="/profile"
                            :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">
                            Account settings
                        </RouterLink>
                    </MenuItem>
                    <MenuItem>
                    <a @click.prevent="signOut"
                        class="hover:bg-gray-100 cursor-pointer block px-4 py-2 text-sm text-gray-700">Sign out</a>
                    </MenuItem>
                </MenuItems>
            </transition>
        </Menu>
    </div>
</template>
<script>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { RouterLink } from 'vue-router'
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline'
import { userStore } from '../stores/user'


export default {
    components:
    {
        Menu,
        MenuButton,
        MenuItem,
        MenuItems,
        RouterLink,
        BellIcon,
    },

    data() {
        return {
            store: userStore(),
            userNavigation: [
                { name: 'Account Settings', href: '#', active: false },
            ]
        };
    },

    computed: {
        icon: {
            get() {
                let idStr = this.store.user.id.toString()
                if (idStr.length === 1)
                    idStr = '00' + idStr
                else if  (idStr.length === 2)
                    idStr = '0' + idStr

                return '/assets/cryptopunks-icons/punk' + idStr + '.png'
            },
        }
    },

    mounted() {

    },

    methods: {
        signOut() {
            localStorage.removeItem('user');
            userStore().user = null
            this.$router.push('/')
        }
    }
};

</script>