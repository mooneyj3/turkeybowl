<template>
    <v-content>
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center" >
                <v-col cols="12" sm="8" md="4">
                    <v-card class="elevation-12">
                        <v-toolbar color="primary" dark flat >
                            <v-toolbar-title>Login form</v-toolbar-title>
                            <div class="flex-grow-1"></div>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field v-model="username" label="Login" name="login" prepend-icon="person" type="text" autocomplete="username"></v-text-field>
                                <v-text-field v-model="password" id="password" label="Password" name="password" prepend-icon="lock" type="password" autocomplete="current-password"></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <div class="flex-grow-1"></div>
                            <v-btn color="warning" v-on:click="goRegisterPage">Register</v-btn>
                            <v-btn color="primary" v-on:click="processLogin">Login</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    export default {
        name: "Login",
        props: {},
        data() {
            return {
                username: "",
                password: ""
            }
        },
        methods: {
            processLogin: function () {
                this.$store.dispatch('login', {username: this.username, password: this.password})
                    .then(() => this.$router.push('/'))

                // this.$store.dispatch('login', data)
                //     .then(() => this.$router.push('/'))
                //     .catch(err => this.console.log(err))
            },
            goRegisterPage: function () { this.$router.push('/register') },

        }
    }
</script>

<style scoped>

</style>
