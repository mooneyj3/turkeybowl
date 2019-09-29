import Vue from 'vue'
import Router from 'vue-router'

import Scoreboard from '@/components/Scoreboard'
import Login from '@/components/pages/Login'
import Profile from '@/components/Profile/Profile'

// import Home from '@/components/pages/Home'
// import Statistica from '@/components/pages/Statistica'
// import TellStory from '@/components/pages/TellStory'
// import ViewCard from '@/components/pages/ViewCard'
// import FindCard from '@/components/pages/FindCard'

Vue.use(Router);

export default new Router({
    // mode: 'history',
    // hash: true,
    routes: [
        {path: '/', name: 'home', component: Scoreboard},
        {path: '/login', name: 'login', component: Login},
        {path: '/profile', name: 'profile', component: Profile}
    ]
})