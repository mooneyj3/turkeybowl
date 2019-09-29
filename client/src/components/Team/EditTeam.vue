<template>
    <v-card class="mx-auto" max-width="600" outlined>
        <v-list-item three-line>
            <v-list-item-content>
                <div class="overline mb-4">EDIT TEAM</div>
                <v-list-item-title class="headline mb-1">The Cosmonauts</v-list-item-title>
                <v-list-item-subtitle>Owner: Rick Sanchez</v-list-item-subtitle>
            </v-list-item-content>
            <!--<v-list-item-avatar tile size="80" color="grey"></v-list-item-avatar>-->
        </v-list-item>

        <v-container class="pa-2" fluid>
            <v-row>
                <v-col>
                    <v-form ref="form" v-model="valid" lazy-validation>
                        <!--<v-text-field v-model="name" :counter="10" :rules="nameRules" label="Name" required></v-text-field>-->
                        <!--<v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>-->

                        <!--<v-select v-model="select" :items="items" :rules="[v => !!v || 'Item is required']" label="Item" required></v-select>-->
                        <!--<v-checkbox v-model="checkbox" :rules="[v => !!v || 'You must agree to continue!']" label="Do you agree?" required></v-checkbox>-->

                        Quarterback
                        <v-checkbox v-model="qb" label="Russell Wilson" value="John"></v-checkbox>
                        <v-checkbox v-model="qb" label="Jackal McGruber" value="Jacob"></v-checkbox>

                        Wide Receiver
                        <v-checkbox v-model="wrcv" label="Your Mom" value="John"></v-checkbox>
                        <v-checkbox v-model="wrcv" label="Poop Skin" value="Jacob"></v-checkbox>

                        Running Back
                        <v-checkbox v-model="rbck" label="Turbo Boost" value="John"></v-checkbox>
                        <v-checkbox v-model="rbck" label="Macklemore" value="Jacob"></v-checkbox>

                        <v-btn :disabled="!valid" color="success" class="mr-4">
                            Validate
                        </v-btn>

                        <v-btn color="error" class="mr-4">
                            Reset Form
                        </v-btn>

                        <v-btn color="warning" @click="resetValidation">
                            Reset Validation
                        </v-btn>
                    </v-form>
                </v-col>
            </v-row>
        </v-container>


    </v-card>
</template>

<script>
    export default {
        name: "Team",
    }
</script>

<style scoped>

</style>