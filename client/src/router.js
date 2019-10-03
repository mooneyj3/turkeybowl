import Vue from 'vue'
import Router from 'vue-router'

import Scoreboard from '@/components/Scoreboard'
import Login from '@/components/Profile/Login'
import Register from '@/components/Profile/Register'
import EditProfile from '@/components/Profile/EditProfile'

import EditTeam from '@/components/Team/EditTeam'
import ViewTeam from '@/components/Team/ViewTeam'

Vue.use(Router);

let router = new Router({
    // mode: 'history',
    // hash: false,
    routes: [
        {path: '/', name: 'home', component: Scoreboard},
        {path: '/login', name: 'login', component: Login},
        {path: '/register', name: 'register', component: Register},
        {path: '/editprofile', name: 'editprofile', component: EditProfile},
        {path: '/editteam', name: 'editteam', component: EditTeam},
        {path: '/team', name: 'team', component: ViewTeam},
    ]
});

export default router
