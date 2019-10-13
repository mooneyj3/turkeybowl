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
                    <v-select v-model="requestType" :items="requestTypes" label="Request Type"></v-select>
                </v-col>
                <v-col>
                    <v-btn color="success">Submit</v-btn>
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

            <v-row>
                <v-sheet elevation="6" class="mx-auto" width="750" color="grey lighten-3">
                    {{ APIResponse === '' ? '...' : APIResponse }}
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
    export default {
        name: "APISandbox",
        data() {
            return {
                username: '',
                password: '',
                endpoint: '',
                headers: '',
                body: '',
                APIResponse: '',
                requestTypes: ['POST', 'GET', 'UPDATE'],
                requestType: '',

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
