import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';


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
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = '';
            state.token = '';
            state.username = '';
        },
    },
    actions: {
        login({commit}, payload) {

            return new Promise((resolve, reject) => {
                commit('auth_request');
                axios({url: 'http://localhost:8000/api/token/', data: payload, method: 'POST'})
                    .then(resp => {
                        const access = resp.data.access;
                        const refresh = resp.data.refresh;
                        const username = payload.username;
                        localStorage.setItem('access', access);
                        localStorage.setItem('refresh', refresh);
                        let data = {token: access, username: username};
                        commit('auth_success', data);
                        resolve(resp);
                    })
                    .catch(err => {
                        commit('auth_error');
                        localStorage.removeItem('access');
                        localStorage.removeItem('refresh');
                        reject(err);
                    });
            });
        },
        logout({commit}, ) {
            commit('logout');
            localStorage.removeItem('access');
            localStorage.removeItem('refresh')
        }
    },
    getters: {
        isLoggedIn: state => !!state.token && !!state.username,
        authStatus: state => state.status,
        username: state => state.username,
    },
});
