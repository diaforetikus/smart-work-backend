<template>
    <div v-if="store.user" class="ml-10 flex items-baseline space-x-4">
        <RouterLink to="/jobs/my"
            :class="[$router.currentRoute.value.path === '/jobs/my' ? 'bg-gray-600 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'px-3 py-2 rounded-md text-sm font-medium']">
            My jobs
        </RouterLink>
        <RouterLink to="/worklist"
            :class="[$router.currentRoute.value.path === '/worklist' ? 'bg-gray-600 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'px-3 py-2 rounded-md text-sm font-medium']">
            Worklist
        </RouterLink>
    </div>
</template>


<script>
import { userStore } from '../stores/user'

export default {


    data() {
        return {
            store: userStore(),
        };
    },
};

</script>