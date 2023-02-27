<template>
    <Teleport to="#header">
        <div class="border-t border-gray-700 py-6">
            <div class="flex justify-between w-full">
                <Categories @selected="selectedCategory" class="flex-1"></Categories>
                <div class="ml-4">
                    <button v-if="store.user" class="btn-secondary" @click="showAddJobModal=true">+ Add job</button>
                    <RouterLink v-else to="/jobs/add">
                        <button class="btn-secondary">+ Add job</button>
                    </RouterLink>
                </div>
            </div>
        </div>
    </Teleport>
    <JobsList :jobs="jobs"></JobsList>
    <AddJobOverlay v-model:show="showAddJobModal"></AddJobOverlay>
</template>

<script>
import Categories from '../components/jobs/Categories.vue'
import JobsList from '../components/jobs/JobsList.vue'
import AddJobOverlay from '../components/jobs/AddJobOverlay.vue'
import { userStore } from '../stores/user'

export default {

    components: {
        Categories,
        JobsList,
        AddJobOverlay
    },

    data() {
        return {
            jobs: [],
            category: null,
            showAddJobModal: false,
            store: userStore()
        }
    },

    mounted() {
        this.loadJobs()
    },

    methods: {
        loadJobs() {
            let loader = this.$loading.show()

            let url = this.apiUrl + "jobs"

            if (this.category)
                url += "?category_id=" + this.category.id

            this.axios
                .get(url)
                .then(response => {
                    this.jobs = response.data
                })
                .catch(error => {
                })
                .finally(() => {
                    loader.hide()
                })
        },

        selectedCategory(category)
        {
            this.category = category
            this.loadJobs()
        }
    }
}
</script>
