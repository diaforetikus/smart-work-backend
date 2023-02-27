import { defineStore } from 'pinia'

export const userStore = defineStore('user', {
    state: () => ({
        user: null,
        account: null,
        balance: null,
    }),

    actions: {
        setUser(user) {
            this.user = user
            this.user.imageUrl = 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80'
            localStorage.setItem('user', JSON.stringify(user))
        },
    },
})