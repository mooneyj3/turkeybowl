import Vue from 'vue'
import Router from 'vue-router'

import Scoreboard from '@/components/Scoreboard'
import Login from '@/components/pages/Login'
import EditProfile from '@/components/Profile/EditProfile'
import EditTeam from '@/components/Team/EditTeam'

Vue.use(Router);

export default new Router({
    // mode: 'history',
    // hash: true,
    routes: [
        {path: '/', name: 'home', component: Scoreboard},
        {path: '/login', name: 'login', component: Login},
        {path: '/editprofile', name: 'editprofile', component: EditProfile},
        {path: '/editteam', name: 'editteam', component: EditTeam}
    ]
})