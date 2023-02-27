<template>
    <nav class="flex space-x-4 ml-10" aria-label="Tabs">
        <a href="#" @click.prevent="setStatus(null)" :class="jobStatus === null ? 'main-tab-active' : 'main-tab'">All</a>
        <a v-if="owner" href="#" @click.prevent="setStatus(1)" :class="jobStatus === 1 ? 'main-tab-active' : 'main-tab'">Open</a>
        <a href="#" @click.prevent="setStatus(2)" :class="jobStatus === 2 ? 'main-tab-active' : 'main-tab'">Waiting</a>
        <a href="#" @click.prevent="setStatus(3)" :class="jobStatus === 3 ? 'main-tab-active' : 'main-tab'">At work</a>
        <a href="#" @click.prevent="setStatus(4)" :class="jobStatus === 4 ? 'main-tab-active' : 'main-tab'">Completed</a>
        <a v-if="owner" href="#" @click.prevent="setStatus(5)" :class="jobStatus === 5 ? 'main-tab-active' : 'main-tab'">Canceled</a>
    </nav>
</template>

<script>

export default {

    props: ["jobs", "owner"],

    emits: ["changed"],

    data() {
        return {
            jobStatus: null
        }
    },

    methods: {
        setStatus(status) {
            this.jobStatus = status
            this.$emit("changed", status)
        }
    }
}
</script>