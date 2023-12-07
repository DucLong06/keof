<template>
	<v-data-table :headers="headers" :items="desserts">
		<template v-slot:top>
			<v-toolbar>
				<!-- <v-toolbar-title>Cá kèo</v-toolbar-title> -->
				<v-divider class="mx-4" inset vertical></v-divider>
				<v-spacer></v-spacer>
				<v-btn
					variant="outlined"
					drak
					class="bg-blue mb-2"
					v-bind="props"
					@click="sendMessage"
				>
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
										<v-combobox
											:items="users"
											label="Chọn người"
											variant="outlined"
											v-model="newItem"
											multiple
											chips
										>
										</v-combobox>
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
			</v-toolbar>
		</template>
		<template v-slot:item.gold="{ item }">
			<div class="flex items-center justify-center gap-x-2">
				<v-icon
					class="text-red"
					icon="mdi-minus-circle"
					@click="minusGold(item)"
				>
				</v-icon>
				<v-chip color="blue"> {{ item.gold }} </v-chip>
				<v-icon
					class="text-green"
					icon="mdi-plus-circle"
					@click="plusGold(item)"
				>
				</v-icon>
			</div>
		</template>
		<template v-slot:item.actions="{ item }">
			<v-icon icon="mdi-delete-circle" @click="deleteItem(item)">
			</v-icon>
		</template>
	</v-data-table>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import ApiService from "./services/api.service";
const dialog = ref(false);
const props = ref();
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
const desserts = ref([]);
const defaultItem = {
	name: "",
	gold: 0,
};
const users = ref([]);
const id_telegram = ref([]);
const newItem = ref([]);
const plusGold = (item) => {
	item.gold = parseInt(item.gold) + 1;
};
const minusGold = (item) => {
	item.gold = parseInt(item.gold) - 1;
};
const deleteItem = (item) => {
	const index = desserts.value.findIndex((dessert) => dessert === item);
	desserts.value.splice(index, 1);
};

const close = () => {
	dialog.value = false;
};

const save = () => {
	newItem.value.forEach((selectedUser, index) => {
		desserts.value.push({
			name: selectedUser,
			id: id_telegram.value[index],
			gold: 0,
		});
	});
	newItem.value = [];
	close();
};

const sendMessage = async () => {
	const transformedObject = {
		items: desserts.value.map(({ id, gold }) => ({ id, gold })),
	};
	const send = await ApiService.sendTelegram(transformedObject);
	if (send.status_code == 200) {
		desserts.value = [];
	} else {
		console.log("bug backend");
	}
};

onMounted(async () => {
	const res = await ApiService.getUser();
	if (res) {
		users.value = res.map((obj) => obj.email);
		id_telegram.value = res.map((obj) => obj.id);
	}
});
</script>

<style scoped></style>
