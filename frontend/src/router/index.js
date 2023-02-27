import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/AboutView.vue')
        },
        {
            path: '/signin',
            name: 'sign in',
            component: () => import('../views/user/SignInView.vue')
        },
        {
            path: '/signup',
            name: 'sign up',
            component: () => import('../views/user/SignUpView.vue')
        },
        {
            path: '/reset-password',
            name: 'reset password',
            component: () => import('../views/user/ResetPasswordView.vue')
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/user/ProfileView.vue')
        },
        {
            path: '/jobs/add',
            name: 'add job',
            component: () => import('../views/jobs/AddJobView.vue')
        },
        {
            path: '/jobs/:id',
            name: 'job show',
            component: () => import('../views/jobs/ShowJobView.vue')
        },
        {
            path: '/jobs/my',
            name: 'my job',
            component: () => import('../views/jobs/MyJobsView.vue')
        },
        {
            path: '/worklist',
            name: 'worklist',
            component: () => import('../views/jobs/WorklListView.vue')
        },
    ]
})


router.beforeEach(async (to, from) => {
    if (!canUserAccess(to)) return '/signin'
    if (isAuth() && ["sign in", "sign up", "reset password"].includes(to.name)) return "/"
})

function canUserAccess(to) {
    if (["home", "sign in", "sign up", "reset password"].includes(to.name) || isAuth())
        return true

    return false
}

function isAuth() {
    const user = JSON.parse(localStorage.getItem('user'))

    if (user && user.token)
        return true

    return false
}

export default router
