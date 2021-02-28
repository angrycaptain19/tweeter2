import Vue from 'vue';
import VueRouter from 'vue-router';
import Feed from '@/views/Feed';
import Auth from '@/views/Auth';
import Profile from '@/views/Profile';
import Discover from '@/views/Discover';

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Feed',
        component: Feed
    },
    {
        path: '/discover',
        name: 'Discover',
        component: Discover
    },
    {
        path: '/auth',
        name: 'Auth',
        component: Auth
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/profile/:id',
        component: Profile
    }
];

const router = new VueRouter({
    routes
});

const protectedRoutes = [
    'Feed',
    'Profile'
];

router.beforeEach((to, from, next) => {
    if (protectedRoutes.includes(to.name) && !Vue.$cookies.get('user')) {
        next({ name: 'Auth'})
    }
    next(); 
});
export default router
