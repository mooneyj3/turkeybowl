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
                                <v-text-field label="Login" name="login" prepend-icon="person" type="text"></v-text-field>
                                <v-text-field id="password" label="Password" name="password" prepend-icon="lock" type="password"></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <div class="flex-grow-1"></div>
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
            return {}
        },
        methods: {
            async processLogin() {
                this.$router.push("/");
                // router.push("/")
            }
        }
    }
</script>

<style scoped>

</style>
