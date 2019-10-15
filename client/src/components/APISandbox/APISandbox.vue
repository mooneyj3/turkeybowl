<template>
    <v-card class="mx-auto" max-width="800">
        <v-card-text>
            <!-- <div>Word of the Day</div> -->
            <p class="display-1 text--primary">
                DEV API Sandbox
            </p>

            <!-- login -->
            <v-row>
                <h2 class="text--primary">LOGIN STATUS</h2>
            </v-row>
            <v-row>
                <v-alert :type="isLoggedIn ? 'success' : 'error'" dense>
                    {{ isLoggedIn ? '' : 'NOT' }} LOGGED IN
                </v-alert>
            </v-row>
            <v-row class="pb-4">
                <v-btn v-if="isLoggedIn" color="warning" @click="processLogout">Logout</v-btn>
                <v-form v-else>
                    <v-container>
                        <v-row>
                            <v-col cols="12" md="4">
                                <v-text-field v-model="username" label="username"></v-text-field>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-text-field v-model="password" label="password" type="password"></v-text-field>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-btn color="success" @click="processLogin">Login</v-btn>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-form>
            </v-row>

            <v-row class="pb-4">
                <h2 class="text--primary">API TEST FIELDS</h2>
            </v-row>

            <v-row>
                <v-col>
                    <v-text-field v-model="endpoint" label="API endpoint"></v-text-field>
                </v-col>
                <v-col>
                    <v-select v-model="method" :items="methods" label="Request Type"></v-select>
                </v-col>
                <v-col>
                    <v-btn color="success" @click="apiRequest">Submit</v-btn>
                </v-col>
            </v-row>

            <v-row>
                <v-textarea v-model="headers" outlined name="input-7-4" label="Headers" value=""></v-textarea>
            </v-row>
            <v-row>
                <v-textarea v-model="body" outlined name="input-7-4" label="Body" value=""></v-textarea>
            </v-row>

            <v-row class="pb-4">
                <h2 class="text--primary">API RESPONSE</h2>
            </v-row>

            <v-row class="pb-4">
                <p><b>Response code:</b> {{ responseCode }}</p>
            </v-row>

            <v-row>
                <v-sheet elevation="6" class="mx-auto" width="750" color="grey lighten-3">
                    {{ responseData === '' ? '...' : responseData }}
                </v-sheet>
            </v-row>


        </v-card-text>
        <!--        <v-card-actions>-->
        <!--            <v-btn text color="deep-purple accent-4">-->
        <!--                Submit-->
        <!--            </v-btn>-->
        <!--        </v-card-actions>-->
    </v-card>
</template>

<script>
    import axios from 'axios'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.defaults.xsrfCookieName = 'csrftoken';

    export default {
        name: "APISandbox",
        data() {
            return {
                username: '',
                password: '',
                endpoint: 'http://localhost:8000/',
                headers: '',
                body: '',
                responseData: '',
                responseCode: '',
                methods: ['POST', 'GET', 'UPDATE'],
                method: 'POST',

            }
        },
        methods: {
            processLogin: function () {
                this.$store.dispatch('login', {username: this.username, password: this.password})
                    .catch(err => {
                        console.log(err)
                    })
            },
            processLogout: function () {
                this.$store.dispatch('logout')
                    .catch(err => {
                        console.log(err)
                    })
            },
            apiRequest() {
                let url = this.endpoint;
                let method = this.method;
                // let headers = this.headers;
                let data = this.body;

                let headers =  {
                    Authorization: 'JWT ' + this.$store.state.token,
                    'Content-Type': 'application/json'
                };

                let isLoggedIn = this.$store.getters.isLoggedIn;

                if (isLoggedIn) {
                    axios.defaults.headers.common['Authorization'] = localStorage.getItem('access');
                }

                axios({url: url, headers: headers, data: data, method: method})
                    .then(resp => {
                        this.responseCode = resp.status;
                        this.responseData = resp.data;
                    })
                    .catch(err => {
                        this.responseCode = err.response.status;
                        this.responseData = err.response.data;
                    })

            }
        },
        computed: {
            isLoggedIn() {
                return this.$store.getters.isLoggedIn
            }
        },

    }
</script>

<style scoped>

</style>
