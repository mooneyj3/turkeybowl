<template>
    <div id="navigation-drawer">
        <v-navigation-drawer v-model="drawer" app right>
            <v-list dense>
                <!--Home-->
                <router-link to="/">
                    <v-list-item>
                        <v-list-item-action>
                            <v-icon>home</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Home</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>

                <!--My Team-->
                <router-link to="/editteam" v-if="isLoggedIn">
                    <v-list-item>
                        <v-list-item-action>
                            <v-icon>people</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Edit My Team</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>

                <!--My Profile-->
                <router-link to="/editprofile" v-if="isLoggedIn">
                    <v-list-item>
                        <v-list-item-action>
                            <v-icon>person</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>My Profile</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>

                <!--login-->
                <router-link to="/login" v-if="!isLoggedIn">
                    <v-list-item>
                        <v-list-item-action>
                            <v-icon>person</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Login</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>

                <!-- logout -->
                <div v-if="isLoggedIn" >
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
        },
        computed: {
            isLoggedIn() {return this.$store.getters.isLoggedIn}
        },
    }
</script>

<style scoped>
    a { text-decoration: none; }
</style>
