import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import Axios from 'axios'
import store from './store.js'

Vue.config.productionTip = false;

Vue.prototype.$http = Axios;

new Vue({
    vuetify,
    router: router,
    render: h => h(App),
    store
}).$mount('#app');
