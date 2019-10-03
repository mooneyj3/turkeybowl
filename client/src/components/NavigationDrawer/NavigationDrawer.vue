<template>
    <div id="navigation-drawer">
        <v-navigation-drawer v-model="drawer" app right>
            <v-list dense>
                <!--Home-->
                <!--<router-link to="/">-->
                <v-list-item @click="goToPage('/')">
                    <v-list-item-action>
                        <v-icon>home</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Home</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <!--</router-link>-->

                <!--My Team-->
                <v-list-item @click="goToPage('/team')" v-if="isLoggedIn">
                    <v-list-item-action>
                        <v-icon>people</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>My Team</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <!--My Profile-->
                <v-list-item @click="goToPage('/editprofile')" v-if="isLoggedIn">
                    <v-list-item-action>
                        <v-icon>person</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>My Profile</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <!--login-->
                <v-list-item @click="goToPage('/login')" v-if="!isLoggedIn">
                    <v-list-item-action>
                        <v-icon>person</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Login</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <!-- logout -->
                <div v-if="isLoggedIn">
                    <v-list-item v-on:click="logout">
                        <v-list-item-action>
                            <v-icon>person</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Logout</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </div>

            </v-list>
        </v-navigation-drawer>
        <v-app-bar app color="primary" dark>
            <div class="flex-grow-1"></div>
            <v-toolbar-title>Turkey Bowl 2019</v-toolbar-title>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        </v-app-bar>
    </div>
</template>

<script>
    export default {
        name: "NavigationDrawer",
        data: () => ({
            drawer: null,
        }),
        methods: {
            logout: function () {
                this.$store.dispatch('logout')
                    .then(() => this.$router.push('/'))
            },
            goToPage: function (destination) {
                this.$router.push(destination).resolve();
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
    a {
        text-decoration: none;
    }
</style>
