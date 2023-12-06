<template>
    <v-data-table :headers="headers" :items="desserts" :sort-by="[{ key: 'gold', order: 'desc' }]">
        <template v-slot:top>
            <v-toolbar flat>
                <!-- <v-toolbar-title>Cá kèo</v-toolbar-title> -->
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>
                <v-btn variant="outlined" drak class="bg-blue  mb-2" v-bind="props">
                    Chốt sổ
                </v-btn>
                <v-dialog v-model="dialog" max-width="500px">
                    <template v-slot:activator="{ props }">
                        <v-btn dark class="bg-green ml-4 mb-2" v-bind="props">
                            Thêm người
                        </v-btn>
                    </template>
                    <v-card>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col cols="12" sm="12" md="12">
                                        <v-combobox :items="[
                                            'California',
                                            'Colorado',
                                            'Florida',
                                            'Georgia',
                                            'Texas',
                                            'Wyoming',
                                        ]" label="Chọn người" variant="outlined" v-model="newItem.name">
                                        </v-combobox>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card-text>

                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue-darken-1" variant="text" @click="close">
                                Thoát
                            </v-btn>
                            <v-btn color="blue-darken-1" variant="text" @click="save">
                                Thêm
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-toolbar>
        </template>
        <template v-slot:item.gold="{ item }">
            <div class="flex items-center justify-center gap-x-2">
                <v-icon class="text-red" icon="mdi-minus-circle" @click="minusGold(item)">
                </v-icon>
                <v-chip color="blue"> {{ item.gold }} </v-chip>
                <v-icon class="text-green" icon="mdi-plus-circle" @click="plusGold(item)">
                </v-icon>
            </div>
        </template>
        <template v-slot:item.actions="{ item }">
            <v-icon icon="mdi-delete-circle" @click="deleteItem(item)">
            </v-icon>
        </template>
        <!-- <template v-slot:no-data>
			<v-btn color="primary" @click="initialize"> Reset </v-btn>
		</template> -->
    </v-data-table>
</template>
<script setup>
import { ref, computed } from "vue";

const dialog = ref(false);
const headers = [
    {
        title: "Tên",
        align: "start",
        sortable: false,
        key: "name",
    },
    { title: "Gold", align: "center", key: "gold" },
    { title: "", align: "center", key: "actions", sortable: false },
];
const desserts = ref([
    { name: "Long", gold: "10" },
    { name: "Long", gold: "20" },
]);

const defaultItem = {
    name: "",
    gold: 0,
};

const newItem = ref(defaultItem)
const plusGold = (item) => {
    item.gold = parseInt(item.gold) + 1
}
const minusGold = (item) => {
    item.gold = parseInt(item.gold) - 1
}
const deleteItem = (item) => {
    const index = desserts.value.findIndex((dessert) => dessert === item);
    desserts.value.splice(index, 1);
};

const close = () => {
    dialog.value = false;
};

const save = () => {
    desserts.value.push({ ...newItem.value });
    newItem.value = defaultItem
    close();
};

const initialize = () => {
    desserts.splice(0, desserts.length);
    // Add your initialization logic here
};

// Additional lifecycle hooks if needed
// onMounted(() => { /* ... */ });
// onUnmounted(() => { /* ... */ });
</script>

<style scoped></style>
