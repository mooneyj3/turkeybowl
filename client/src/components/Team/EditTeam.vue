<template>
    <v-card class="mx-auto" max-width="600" outlined>
        <v-list-item three-line>
            <v-list-item-content>
                <div class="overline mb-4">EDIT TEAM</div>
                <v-list-item-title class="headline mb-1">The Cosmonauts</v-list-item-title>
                <v-list-item-subtitle>Owner: {{ getUsername }}</v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>

        <v-container class="pa-2" fluid>
            <v-row>
                <v-col>
                    <h2>Quarterback</h2>
                    <p>Select one</p>
                    <PositionSelectTable v-bind:players="quarterbacks"></PositionSelectTable>

                    <v-divider></v-divider>
                    <h2>Wide Receivers</h2>
                    <p>Select two</p>
                    <PositionSelectTable v-bind:players="wideReceivers"></PositionSelectTable>
                </v-col>
            </v-row>
        </v-container>


    </v-card>
</template>

<script>
    import PositionSelectTable from "./PositionSelectTable";

    export default {
        name: "Team",
        components: {PositionSelectTable},
        data() {
            return {
                quarterbacks: [
                    {name: 'Mitch Trubisky', team: 'CHI', espnID: '3039707'},
                    {name: 'Matthew Stafford', team: 'DET', espnID: '12483'},
                ],
                wideReceivers: [
                    {name: 'Allen Robinson II', team: 'CHI', espnID: '16799'},
                    {name: 'Taylor Gabriel', team: 'CHI', espnID: '17437'},
                    {name: 'Anthony Miller', team: 'CHI', espnID: '3050487'},
                    {name: 'Kenny Golladay', team: 'DET', espnID: '2974858'},
                    {name: 'Marvin Jones Jr.', team: 'DET', espnID: '15072'},
                    {name: 'Danny Amendola', team: 'DET', espnID: '11674'},
                ],

            }
        },
        computed: {
            getUsername() {
                return this.$store.getters.username
            },
        },

    }
</script>

<style scoped>

</style>
