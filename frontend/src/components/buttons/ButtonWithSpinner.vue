<template>
    <button type="submit" :disabled="loading" :class="'btn-primary mt-2 ' + (loading ? 'disabled:opacity-40' : '')">
        <span v-if="!loading">{{ text }}</span>
        <LoadingIcon v-else></LoadingIcon>
    </button>
</template>

<script>

    import LoadingIcon from "../icons/LoadingIcon.vue"

    export default {
        components: {
            LoadingIcon
        },
        
        props: ['loading', 'text'],
    }
</script>