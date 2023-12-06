<template>
	<v-data-table
		:headers="headers"
		:items="desserts"
		:sort-by="[{ key: 'calories', order: 'asc' }]"
	>
		<template v-slot:top>
			<v-toolbar flat>
				<v-toolbar-title>Cá kèo</v-toolbar-title>
				<v-divider class="mx-4" inset vertical></v-divider>
				<v-spacer></v-spacer>
				<v-dialog v-model="dialog" max-width="500px">
					<template v-slot:activator="{ props }">
						<v-btn color="primary" dark class="mb-2" v-bind="props">
							Thêm người
						</v-btn>
					</template>
					<v-card>
						<v-card-text>
							<v-container>
								<v-row>
									<v-col cols="12" sm="12" md="12">
										<v-combobox
											:items="[
												'California',
												'Colorado',
												'Florida',
												'Georgia',
												'Texas',
												'Wyoming',
											]"
											label="Chọn người"
											variant="outlined"
										></v-combobox>
									</v-col>
								</v-row>
							</v-container>
						</v-card-text>

						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn
								color="blue-darken-1"
								variant="text"
								@click="close"
							>
								Thoát
							</v-btn>
							<v-btn
								color="blue-darken-1"
								variant="text"
								@click="save"
							>
								Thêm
							</v-btn>
						</v-card-actions>
					</v-card>
				</v-dialog>
				<v-dialog v-model="dialogDelete" max-width="500px">
					<v-card>
						<v-card-title class="text-h5"
							>Are you sure you want to delete this
							item?</v-card-title
						>
						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn
								color="blue-darken-1"
								variant="text"
								@click="closeDelete"
								>Cancel</v-btn
							>
							<v-btn
								color="blue-darken-1"
								variant="text"
								@click="deleteItemConfirm"
								>OK</v-btn
							>
							<v-spacer></v-spacer>
						</v-card-actions>
					</v-card>
				</v-dialog>
			</v-toolbar>
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
const dialogDelete = ref(false);
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
const desserts = [
	{ name: "Long", gold: "10" },
	{ name: "Long", gold: "10" },
];

const editedIndex = ref(-1);
const editedItem = ref({
	name: "",
	gold: 0,
});

const defaultItem = {
	name: "",
	gold: 0,
};

const formTitle = computed(() => {
	return editedIndex.value === -1 ? "New Item" : "Edit Item";
});

const deleteItem = (item) => {
	editedIndex.value = desserts.indexOf(item);
	editedItem.value = { ...item };
	dialogDelete.value = true;
};

const deleteItemConfirm = () => {
	desserts.value = desserts.splice(editedIndex.value, 1);
	closeDelete();
};

const close = () => {
	dialog.value = false;
	editedItem.value = { ...defaultItem };
	editedIndex.value = -1;
};

const closeDelete = () => {
	dialogDelete.value = false;
	editedItem.value = { ...defaultItem };
	editedIndex.value = -1;
};

const save = () => {
	if (editedIndex.value > -1) {
		Object.assign(desserts[editedIndex.value], editedItem.value);
	} else {
		desserts.push({ ...editedItem.value });
	}
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
