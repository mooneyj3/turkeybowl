import Vue from "vue";
import Vuex from "vuex";


Vue.use(Vuex);
export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        username: '',
    },
    mutations: {
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, payload){
            state.status = 'success';
            state.token = payload.token;
            state.username = payload.username;
        },
        logout(state){
            state.status = '';
            state.token = '';
            state.username = '';
        },
    },
    actions: {
        login({commit}, payload) {
            commit('auth_request');

            let username = payload.username;
            // let password = payload.password;
            let token = 'test_jwt';

            localStorage.setItem('token', 'test_jwt');
            let data = {token: token, username: username};

            commit('auth_success', data)
        },
        logout({commit}, ) {
            commit('logout');
            localStorage.removeItem('token');
        }
    },
    getters: {
        isLoggedIn: state => !!state.token && !!state.username,
        authStatus: state => state.status,
        username: state => state.username,
    },
});
