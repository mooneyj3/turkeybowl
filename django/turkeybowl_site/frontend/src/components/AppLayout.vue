<template>
    <v-app id="inspire">
        <NavigationDrawer></NavigationDrawer>

        <v-content>
            <router-view></router-view>
            <!--<v-container class="fill-height" fluid>-->
            <!--<v-row justify="center" align="center">-->
            <!--<v-col class="text-center">-->
            <!--<v-tooltip left>-->
            <!--<template v-slot:activator="{ on }">-->
            <!--<v-btn-->
            <!--:href="source"-->
            <!--icon-->
            <!--large-->
            <!--target="_blank"-->
            <!--v-on="on"-->
            <!--&gt;-->
            <!--<v-icon large>mdi-code-tags</v-icon>-->
            <!--</v-btn>-->
            <!--</template>-->
            <!--<span>Source</span>-->
            <!--</v-tooltip>-->

            <!--<v-tooltip right>-->
            <!--<template v-slot:activator="{ on }">-->
            <!--<v-btn icon large href="https://codepen.io/johnjleider/pen/WVbPgz" target="_blank" v-on="on">-->
            <!--<v-icon large>mdi-codepen</v-icon>-->
            <!--</v-btn>-->
            <!--</template>-->
            <!--<span>Codepen</span>-->
            <!--</v-tooltip>-->
            <!--</v-col>-->
            <!--</v-row>-->
            <!--</v-container>-->
        </v-content>

        <v-footer color="primary" app>
            <div class="flex-grow-1"></div>
            <span class="white--text">&copy; 2019</span>
        </v-footer>
    </v-app>
</template>


<!--<template>-->
<!--<div class="app-layout">-->
<!--<h1>App Layout</h1>-->
<!--<p>You've got some work to do.</p>-->
<!--<router-view></router-view>-->
<!--</div>-->
<!--</template>-->


<script>
    import NavigationDrawer from "./NavigationDrawer/NavigationDrawer";
    export default {
        name: "AppLayout",
        components: {NavigationDrawer},
        props: {
            source: String,
        },
        // data: () => ({
        //     drawer: null,
        // }),
    }
</script>


<style scoped>
</style>
