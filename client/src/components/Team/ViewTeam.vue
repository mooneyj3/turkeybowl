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
                    <th class="text-center">Add</th>
                    <th class="text-center">Drop</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(value, key) in team" :key="value.id">
                    <td>{{ key }}</td>
                    <td>{{ value.name }}</td>
                    <td><v-img class="pr-0" :src="logos[value.team]" max-width="25" max-height="30"></v-img></td>
                    <td class="text-center">
                        <SelectPlayer
                                v-if="value.pos === 'WR'"
                                v-bind:pos="value.pos"
                                @selectPlayer="updatePlayer(key, ...arguments)">
                        </SelectPlayer>
                    </td>
                    <td class="text-center"><v-icon color="error">remove_circle</v-icon></td>
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
                team: {
                    QB: {name: '', team: '', id: 1, pos: 'QB'},
                    RB: {name: '', team: '', id: 2, pos: 'RB'},
                    WR: {name: '', team: '', id: 3, pos: 'WR'},
                    TE: {name: '', team: '', id: 4, pos: 'TE'},
                    K: {name: '', team: '', id: 5, pos: 'K'},
                    DST: {name: '', team: '', id: 6, pos: 'DST'},
                },
                logos: {
                    CHI: 'logos/bears.png',
                    BUF: 'logos/bills.png',
                    DAL: 'logos/cowboys.png',
                    ATL: 'logos/falcons.png',
                    DET: 'logos/lions.png',
                    NO: 'logos/saint.png',
                }

            }
        },
        methods: {
            // goEditTeamPage: function () { this.$router.push('/editteam') },
            updatePlayer: function (position, item) {
                this.team[position] = item;
            }
        }
    }
</script>

<style scoped>
</style>
