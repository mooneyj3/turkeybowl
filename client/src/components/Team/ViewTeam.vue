<template>
    <v-card class="mx-auto" max-width="600" outlined>
        <v-list-item two-line>
            <v-list-item-content>
                <v-list-item-title class="headline mb-1">Team Name</v-list-item-title>
                <v-list-item-subtitle>Team Owner</v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>
        <v-simple-table>
            <template v-slot:default>
                <thead>
                <tr>
                    <th class="text-left">Position</th>
                    <th class="text-left">Name</th>
                    <th class="text-left">Team</th>
                    <th class="text-center">Add / Drop</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(value, key) in selectedPlayers" :key="key">
                    <td>{{ key }}</td>
                    <td>{{ value !== null ? value.name : '' }}</td>
                    <td>
                        <v-img v-if="value !== null" class="pr-0" :src="logos[value.team]" max-width="25" max-height="30"></v-img>
                    </td>
                    <td class="text-center">
                        <v-row>
                            <div class="flex-grow-1"></div>
                            <SelectPlayer
                                    v-bind:position="key"
                                    v-bind:teamFilter="teamFilter"
                                    @selectPlayer="updatePlayer(key, ...arguments)">
                            </SelectPlayer>
                            <div class="flex-grow-1 hidden-md-and-up"></div>
                            <v-icon color="error" class="mx-auto" v-on:click="removePlayer(key)">
                                remove_circle
                            </v-icon>
                            <div class="flex-grow-1"></div>
                        </v-row>
                    </td>
                </tr>
                </tbody>
            </template>
        </v-simple-table>
    </v-card>
</template>

<script>
    import SelectPlayer from "./SelectPlayer";

    export default {
        name: "ViewTeam",
        components: {SelectPlayer},
        data() {
            return {
                teamFilter: {
                    CHI: false,
                    BUF: false,
                    DAL: false,
                    ATL: false,
                    DET: false,
                    NO: false,
                },
                selectedPlayers: {
                    QB: null,
                    RB: null,
                    WR: null,
                    TE: null,
                    K: null,
                    DST: null,
                },
                logos: {
                    CHI: 'logos/bears.png',
                    BUF: 'logos/bills.png',
                    DAL: 'logos/cowboys.png',
                    ATL: 'logos/falcons.png',
                    DET: 'logos/lions.png',
                    NO: 'logos/saints.png',
                }

            }
        },
        methods: {
            // goEditTeamPage: function () { this.$router.push('/editteam') },
            updatePlayer: function (position, item) {
                this.teamFilter[item.team] = true;
                this.selectedPlayers[position] = item;
            },
            removePlayer: function (position) {
                if (this.selectedPlayers[position] === null) return;

                // extract the team
                let team = this.selectedPlayers[position].team;

                this.teamFilter[team] = false;
                this.selectedPlayers[position] = null;
            }
        }
    }
</script>

<style scoped>
</style>
