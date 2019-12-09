import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'MainHomePage',
            component: () => import('./components/MainHomePage.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/User',
            name: 'User',
            component: () => import('./components/auth/User.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/User/SignUp',
            name: 'SignUp',
            component: () => import('./components/auth/SignUp.vue'),
            meta: { requiresAuth: true }
        },
    ]
})