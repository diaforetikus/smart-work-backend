<template>
    <ul role="list" class="space-y-10">
        <li v-for="job in jobs" :key="job.id" class="bg-white px-4 py-6 shadow sm:rounded-lg sm:px-6 border-transparent border-2 hover:border-green-500">
            <div class="sm:flex sm:items-baseline sm:justify-between">
                <h2 class="font-medium text-2xl">
                    <RouterLink :to="'/jobs/' + job.id" class="text-gray-900">
                        {{ job.title }}
                    </RouterLink>
                </h2>
                <p class="mt-1 whitespace-nowrap text-sm text-gray-600 sm:mt-0 sm:ml-3">
                    <time :datetime="moment(job.created_at).format('MMMM Do YYYY, h:mm')">{{ moment(job.created_at).format("MMMM Do YYYY, h:mm") }}</time>
                </p>
            </div>
            <div class="mt-4 space-y-6 text-gray-800">
                <p>{{ job.description }}</p>
            </div>
            <div class="mt-4 font-medium text-gray-500 text-sm">
                Posted by {{ job.owner.first_name + " " + job.owner.last_name }}
            </div>

            <div class="border-t border-gray-200 py-4 mt-4 text-sm">
                <div class="flex justify-between">
                    <dl class="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-3">
                        <div class="sm:col-span-1">
                            <dt class="font-medium text-gray-500">Salary expectation</dt>
                            <div class="flex items-center">
                                <img src="/assets/tether.svg" class="w-5 h-5 mr-1 mt-0.5 block" />
                                <dd class="mt-1 text-gray-900 font-medium">
                                    ${{ job.amount }}
                                </dd>
                            </div>
                        </div>
                        <div class="sm:col-span-1 w-72">
                            <dt class="font-medium text-gray-500">Job category</dt>
                            <dd class="mt-1 text-gray-900">{{ job.category.name }}</dd>
                        </div>
                    </dl>
                    <div>
                        <span v-if="job.status != 'open'" :class="'inline-flex items-center rounded-full px-3 py-0.5 text-sm font-medium ' + getBadgeColor(job.status)">{{ job.status }}</span>        
                    </div>
                </div>
            </div>
        </li>
    </ul>
</template>

<script>
import moment from 'moment'
import {getBadgeColor} from '../../utils'

export default {

    props: ["jobs"],

    data() {
        return {
            moment: moment,
            getBadgeColor: getBadgeColor
        }
    },

    methods: {
    }
}
</script>
