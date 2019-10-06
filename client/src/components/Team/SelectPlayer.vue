<template>
    <v-row justify="center">
        <v-dialog persistent v-model="dialog" scrollable max-width="300px">
            <template v-slot:activator="{ on }">
                <v-icon color="green" v-on="on">add_circle</v-icon>
<!--                <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
            </template>
            <v-card>
                <v-card-title>Select a {{ pos }}</v-card-title>
                <v-divider></v-divider>
                <v-card-text style="height: 300px;">
                    <v-radio-group v-model="selectedPlayer" column>
                        <v-radio v-for="player in players"
                                 :label="player.name + '\t(' + player.team + ')'"
                                 :key=player.espnID
                                 :value=player
                        >

                        </v-radio>
<!--                        <v-radio label="Bahamas, The" value="bahamas"></v-radio>-->
<!--                        <v-radio label="Bahrain" value="bahrain"></v-radio>-->
<!--                        <v-radio label="Bangladesh" value="bangladesh"></v-radio>-->
<!--                        <v-radio label="Barbados" value="barbados"></v-radio>-->
<!--                        <v-radio label="Belarus" value="belarus"></v-radio>-->
<!--                        <v-radio label="Belgium" value="belgium"></v-radio>-->
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
        props: ['pos'],
        data() {
            return {
                selectedPlayer: '',
                dialog: false,
                players: [
                    {name: 'Allen Robinson II', team: 'CHI', id: '16799', pos: 'WR'},
                    {name: 'Taylor Gabriel', team: 'CHI', id: '17437', pos: 'WR'},
                    {name: 'Anthony Miller', team: 'CHI', id: '3050487', pos: 'WR'},
                    {name: 'Kenny Golladay', team: 'DET', id: '2974858', pos: 'WR'},
                    {name: 'Marvin Jones Jr.', team: 'DET', id: '15072', pos: 'WR'},
                    {name: 'Danny Amendola', team: 'DET', id: '11674', pos: 'WR'},
                ],
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
