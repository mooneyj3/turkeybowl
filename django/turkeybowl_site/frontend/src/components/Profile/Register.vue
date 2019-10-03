<template>
    <v-content>
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center" >
                <v-col cols="12" sm="8" md="4">
                    <v-card class="elevation-12">
                        <v-toolbar color="primary" dark flat >
                            <v-toolbar-title>Registration form</v-toolbar-title>
                            <div class="flex-grow-1"></div>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field v-model="username" label="username" name="User Name" prepend-icon="person" type="text" autocomplete="username"></v-text-field>
                                <v-text-field v-model="teamName" id="teamName" label="Team Name" name="teamName" prepend-icon="people" type="text"></v-text-field>
                                <v-text-field v-model="password" id="password" label="Password" name="password" prepend-icon="lock" type="password" autocomplete="new-password"></v-text-field>
                                <v-text-field v-model="confirmPassword" id="confirmPassword" label="Confirm Password" name="confirmPassword" prepend-icon="lock" type="password" autocomplete="new-password"></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <div class="flex-grow-1"></div>
                            <v-text-field v-model="leaguePassword" id="leaguePassword" label="League Password" name="leaguePassword" prepend-icon="" type="text"></v-text-field>
                            <v-btn color="success" v-on:click="submitRegistration">Register</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    export default {
        name: "Register",
        props: {},
        data() {
            return {
                username: "",
                password: "",
                confirmPassword: "",
                teamName: "",
                leaguePassword: "",
            }
        },
        methods: {
            submitRegistration: function () {
                this.$router.push('/');
                // this.$store.dispatch('login', {username: this.username, password: this.password})
                //     .then(() => this.$router.push('/'))

                // this.$store.dispatch('login', data)
                //     .then(() => this.$router.push('/'))
                //     .catch(err => this.console.log(err))
            }
        }
    }
</script>

<style scoped>

</style>
