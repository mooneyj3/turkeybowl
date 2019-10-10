<template>
    <v-row justify="center">
        <v-dialog persistent v-model="dialog" scrollable max-width="300px">
            <template v-slot:activator="{ on }">
                <v-icon color="success" v-on="on">add_circle</v-icon>
            </template>
            <v-card>
                <v-card-title>Select a {{ position }}</v-card-title>
                <v-divider></v-divider>
                <v-card-text style="height: 300px;">
                    <v-radio-group v-model="selectedPlayer" column>
                        <v-radio v-for="player in activePosition"
                                 :label="player.name + '\t(' + player.team + ')'"
                                 :key=player.espnID
                                 :value=player
                                 :disabled="teamFilter[player.team]"
                        >
                        </v-radio>
                    </v-radio-group>
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-btn color="error darken-1" text @click="cancel">Cancel</v-btn>
                    <v-btn color="success darken-1" text @click="save">Save</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script>
    export default {
        name: "SelectPlayer",
        props: {
            position: String,
            teamFilter: Object,
        },
        data() {
            return {
                selectedPlayer: '',
                dialog: false,
                players: [
                    {name: 'Mitchell Trubisky', team: 'CHI', id: '3039707', pos: 'QB'},
                    {name: 'Matthew Stafford', team: 'DET', id: '', pos: 'QB'},
                    {name: 'Josh Allen', team: 'BUF', id: '', pos: 'QB'},
                    {name: 'Dak Prescott', team: 'DAL', id: '', pos: 'QB'},
                    {name: 'Matt Ryan', team: 'ATL', id: '', pos: 'QB'},
                    {name: 'Teddy Bridgewater', team: 'NO',  id: '', pos: 'QB'},

                    {name: 'David Montgomery', team: 'CHI', id: '4035538', pos: 'RB'},
                    {name: 'Kerryon Johnson', team: 'DET', id: '', pos: 'RB'},
                    {name: 'Frank Gore', team: 'BUF', id: '', pos: 'RB'},
                    {name: 'Ezekiel Elliott', team: 'DAL', id: '', pos: 'RB'},
                    {name: 'Devonta Freeman', team: 'ATL', id: '', pos: 'RB'},
                    {name: 'Alvin Kamara', team: 'NO',  id: '', pos: 'RB'},

                    {name: 'Allen Robinson II', team: 'CHI', id: '16799', pos: 'WR'},
                    {name: 'Kenny Golladay', team: 'DET', id: '2974858', pos: 'WR'},
                    {name: 'John Brown', team: 'BUF', id: '', pos: 'WR'},
                    {name: 'Amari Cooper', team: 'DAL', id: '', pos: 'WR'},
                    {name: 'Julio Jones', team: 'ATL', id: '', pos: 'WR'},
                    {name: 'Michael Thomas', team: 'NO',  id: '', pos: 'WR'},

                    {name: 'Trey Burton', team: 'CHI', id: '', pos: 'TE'},
                    {name: 'T.J. Hockenson', team: 'DET', id: '', pos: 'TE'},
                    {name: 'Tyler Kroft', team: 'BUF', id: '', pos: 'TE'},
                    {name: 'Jason Witten', team: 'DAL', id: '', pos: 'TE'},
                    {name: 'Austin Hooper', team: 'ATL', id: '', pos: 'TE'},
                    {name: 'Jared Cook', team: 'NO',  id: '', pos: 'TE'},

                    {name: 'Eddy Pineiro', team: 'CHI', id: '', pos: 'K'},
                    {name: 'Matt Prater', team: 'DET', id: '', pos: 'K'},
                    {name: 'Stephen Hauschka', team: 'BUF', id: '', pos: 'K'},
                    {name: 'Brett Maher', team: 'DAL', id: '', pos: 'K'},
                    {name: 'Matt Bryant', team: 'ATL', id: '', pos: 'K'},
                    {name: 'Wil Lutz', team: 'NO',  id: '', pos: 'K'},

                    {name: 'Bears', team: 'CHI', id: '', pos: 'DST'},
                    {name: 'Lions', team: 'DET', id: '', pos: 'DST'},
                    {name: 'Bills', team: 'BUF', id: '', pos: 'DST'},
                    {name: 'Cowboys', team: 'DAL', id: '', pos: 'DST'},
                    {name: 'Falcons', team: 'ATL', id: '', pos: 'DST'},
                    {name: 'Saints', team: 'NO',  id: '', pos: 'DST'},

                    {name: '', team: 'CHI', id: '', pos: ''},
                    {name: '', team: 'DET', id: '', pos: ''},
                    {name: '', team: 'BUF', id: '', pos: ''},
                    {name: '', team: 'DAL', id: '', pos: ''},
                    {name: '', team: 'ATL', id: '', pos: ''},
                    {name: '', team: 'NO',  id: '', pos: ''},
                ],
            }
        },
        computed: {
            activePosition() {
                return this.players.filter(player => player.pos === this.position);
            },
            filterTeam(player) {
                return this.teamFilter[player.team]
            }
        },
        methods: {
            cancel: function() {
                this.dialog = false;
            },
            save: function() {
                this.dialog = false;
                this.$emit('selectPlayer', this.selectedPlayer)
            }
        }
    }
</script>

<style scoped>

</style>
