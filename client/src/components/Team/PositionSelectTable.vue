<template>
    <div>
        <v-data-table v-model="selected"
                      :headers="headers"
                      :items="players"
                      item-key="espnID"
                      class="elevation-2"
                      :disable-pagination="true"
                      :hide-default-footer="true"
                      show-select
                      dense
        >
            <!-- header.data-table-select -->
            <template v-slot:header.data-table-select=""></template>
            <template v-slot:item.data-table-select="{ isSelected, select }" >
<!--                <v-simple-checkbox hide-details :value="isSelected" @input="select($event)"></v-simple-checkbox>-->
                <v-checkbox hide-details class="mt-0" :value="isSelected" @change="selectRow($event)"></v-checkbox>
            </template>
<!--            <template v-slot:default:item="props"></template>-->
<!--            <template v-slot:item="props">-->
<!--                <tr>-->
<!--                    <td>{{ props.item.name }}</td>-->
<!--                    <td>{{ props.item.team }}</td>-->
<!--                </tr>-->
<!--            </template>-->

        </v-data-table>

    </div>
</template>

<script>
    export default {
        name: "PositionSelectTable",
        props: ['players'],
        data() {
            return {
                selected: [],
                headers: [
                    {text: 'Name', align: 'left', value: 'name'},
                    {text: 'Team', align: 'left', value: 'team'},
                ],
            }
        },
        methods: {
            selectRow: function (item) {
                this.selected.push(item)
            }
        }
    }
</script>

<style scoped>

</style>
