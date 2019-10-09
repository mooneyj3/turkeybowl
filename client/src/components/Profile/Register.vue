<template>
    <v-content>
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-col cols="12" sm="8" md="4">
                    <v-card class="elevation-12">
                        <v-toolbar color="primary" dark flat>
                            <v-toolbar-title>Registration form</v-toolbar-title>
                            <div class="flex-grow-1"></div>
                        </v-toolbar>
                        <v-card-text>
                            <v-form @submit.prevent="submitRegistration" id="registration-form" ref="form"
                                    v-model="valid" lazy-validation>

                                <h2>Login Details</h2>
                                <p>This information <b>will not be visible</b> others in the league.</p>

                                <!-- username -->
                                <v-text-field v-model="username" :rules="usernameRules" label="User Name"
                                              name="username" prepend-icon="person" type="text"
                                              autocomplete="username" required>
                                </v-text-field>

                                <!-- password -->
                                <v-text-field :rules="genericRules" v-model="password" id="password" label="Password"
                                              name="password" prepend-icon="lock" type="password"
                                              autocomplete="new-password" required>
                                </v-text-field>

                                <!-- password -->
                                <v-text-field :rules="genericRules" v-model="confirmPassword" id="confirmPassword"
                                              label="Confirm Password" name="confirmPassword"
                                              prepend-icon="lock" type="password"
                                              autocomplete="new-password" required>
                                </v-text-field>

                                <!-- Team info section -->
                                <v-divider color="darkgrey" class="mx-0 pb-1 mt-5 mb-3"></v-divider>
                                <h2 class="pt-5">Team Information</h2>
                                <p>This information <b>will be visible</b> do other players in the league.</p>

                                <!-- team name -->
                                <v-text-field :rules="genericRules" v-model="teamName" id="teamName" label="Team Name"
                                              name="teamName" prepend-icon="people" type="text" required>
                                </v-text-field>

                                <!-- display name -->
                                <v-text-field :rules="genericRules" v-model="displayName" id="displayName"
                                              label="Display Name"
                                              name="displayName" prepend-icon="people" type="text" required>
                                </v-text-field>

                                <v-divider color="darkgrey" class="mx-0 pb-1 mt-5 mb-5"></v-divider>

                                <!-- league password -->
                                <v-text-field :rules="genericRules" v-model="leaguePassword" id="leaguePassword"
                                              label="League Password" name="leaguePassword" prepend-icon=""
                                              type="text" ></v-text-field>

                            </v-form>

                            <v-alert class="mt-5" v-if="(submitErrors.length > 0)" type="error">
                                <ul>
                                    <li v-for="(e, index) in submitErrors" :key="index">
                                        {{e}}
                                    </li>
                                </ul>
                            </v-alert>

                        </v-card-text>

                        <v-card-actions>
                            <!-- submit button -->
                            <div class="flex-grow-1"></div>
                            <v-btn type="submit" form="registration-form" color="primary">
                                Register
                            </v-btn>

                            <div class="flex-grow-1"></div>
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
                valid: false,
                username: "",
                usernameRules: [
                    v => !!v || 'User Name is Required',
                    v => (v.length >= 5 && v.length < 20) || 'User Name must be 5-20 characters long',
                    v => /^[a-zA-Z0-9_]*$/.test(v) || 'User Name must be letters and numbers only',
                ],
                password: "",
                confirmPassword: "",
                teamName: "",
                displayName: "",
                leaguePassword: "",
                genericRules: [
                    v => !!v || 'This field is Required',
                ],
                submitErrors: [],
            }
        },
        methods: {
            submitRegistration() {
                // validate the form
                this.submitErrors = [];
                let validForm = this.$refs.form.validate();
                if (!validForm) {this.submitErrors.push("Incorrect/Missing Form Fields")}

                let validPassword = this.password === this.confirmPassword;
                if (!validPassword) {
                    this.submitErrors.push("Passwords do not match");
                }

                if (this.$refs.form.validate()) {
                    this.$router.push('/');
                }

                // this.$refs.form.checkValidity();


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
    h2 {
        color: black;
    }

</style>
