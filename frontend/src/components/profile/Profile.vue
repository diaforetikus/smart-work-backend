<template>
    <div>
        <Teleport to="#header">
            <nav class="flex space-x-4 border-t border-gray-700 py-4"  aria-label="Tabs">
                <a @click.prevent="currentTab = 'about'" href="#"
                    :class="'main-tab' + (currentTab === 'about' ? '-active' : '')">
                    About
                </a>
                <a @click.prevent="currentTab = 'account_security'" href="#"
                    :class="'main-tab' + (currentTab === 'account_security' ? '-active' : '')">
                    Account security
                </a>
                <a @click.prevent="currentTab = 'account_email'" href="#"
                    :class="'main-tab' + (currentTab === 'account_email' ? '-active' : '')">
                    E-mail
                </a>
            </nav>
        </Teleport>
        <div class="flex justify-center">
            <div class="flex-1 max-w-2xl">
                <div v-if="currentTab === 'about'">
                    <About></About>
                </div>
                <div v-else-if="currentTab === 'account_security'">
                    <Security></Security>
                </div>
                <div v-else-if="currentTab === 'account_email'">
                    <Email></Email>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import About from './About.vue'
    import Security from './Security.vue'
    import Email from './Email.vue'

    export default {
        components: {
            About,
            Security,
            Email,
        },

        data() {
            return {
                currentTab: 'about',
            }
        },

        mounted() {
        },

        methods: {
        }

    }
</script>