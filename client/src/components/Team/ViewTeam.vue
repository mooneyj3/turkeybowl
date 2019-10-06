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
                    <th class="text-center">Add/Change</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(value, key) in team" :key="value.id">
                    <td>{{ key }}</td>
                    <td>{{ value.name }}</td>
                    <td>{{ value.team }}</td>
                    <td class="text-center">
                        <SelectPlayer
                                v-if="value.pos === 'WR'"
                                v-bind:pos="value.pos"
                                @selectPlayer="updatePlayer(key, ...arguments)">
                        </SelectPlayer>
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
                team: {
                    QB: {name: '', team: '', id: 1, pos: 'QB'},
                    RB1: {name: '', team: '', id: 2, pos: 'RB'},
                    RB2: {name: '', team: '', id: 3, pos: 'RB'},
                    WR1: {name: '', team: '', id: 4, pos: 'WR'},
                    WR2: {name: '', team: '', id: 5, pos: 'WR'},
                    TE: {name: '', team: '', id: 6, pos: 'TE'},
                    K: {name: '', team: '', id: 7, pos: 'K'},
                    DST: {name: '', team: '', id: 8, pos: 'DST'},
                },

            }
        },
        methods: {
            // goEditTeamPage: function () { this.$router.push('/editteam') },
            updatePlayer: function(position, item) {
                this.team[position] = item;
            }
        }
    }
</script>

<style scoped>

</style>
