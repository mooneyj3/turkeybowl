<template>
    <div class="scoreboard">
        <div v-if="getUsername === ''">
            <h1>Looks like you're not logged in</h1>
            <p><router-link to="/login">Please login here</router-link></p>
        </div>
        <div v-else>
            <h1>Hello {{ getUsername }}</h1>
            <p>Welcome to Turkey Bowl 2019!!!</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Scoreboard",
        props: {},
        data() {
            return {}
        },
        computed: {
            getUsername() {
                return this.$store.state.username;
            }
        }

    }
</script>

<style scoped>

</style>
