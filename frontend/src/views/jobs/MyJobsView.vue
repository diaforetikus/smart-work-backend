<template>
    <Teleport to="#header">
        <div class="border-t border-gray-700 py-6">
            <div class="flex justify-between w-full items-center">
                <Categories @selected="selectedCategory" class="flex-1"></Categories>
                <Tabs :owner="true" @changed="changedStatus"></Tabs>
            </div>
        </div>
    </Teleport>
    <JobsList :jobs="jobs"></JobsList>
</template>

<script>
import Categories from '../../components/jobs/Categories.vue'
import JobsList from '../../components/jobs/JobsList.vue'
import Tabs from '../../components/jobs/Tabs.vue'

export default {

    components: {
        Categories,
        JobsList,
        Tabs
    },

    data() {
        return {
            jobs: [],
            category: null,
            jobStatus: null,
        }
    },

    mounted() {
        this.loadJobs()
    },

    methods: {
        loadJobs() {
            let loader = this.$loading.show()

            let url = this.apiUrl + "jobs/my"

            let params = ""

            if (this.category)
                params += "&category_id=" + this.category.id

            if (this.jobStatus)
                params += "&status_id=" + this.jobStatus

            if (params && !params.includes("?"))
                params = "?" + params.substring(1);

            url += params

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
        },

        changedStatus(status) {
            this.jobStatus = status
            this.loadJobs()
        }
    }
}
</script>
