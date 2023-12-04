import json


def read_data_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_data_json(file_path, data_to_append):
    try:
        existing_data = read_data_json(file_path)

        existing_data.extend(data_to_append)

        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=2)
    except Exception as e:
        return


def update_user_data(file_path, user_id, bank, account_number):
    with open(file_path, 'r') as file:
        user_data = json.load(file)

    user_index = None
    # Find the user with the given ID
    for index, user in enumerate(user_data):
        if str(user.get("id")) == user_id:
            user_index = index
            break

    if user_index is not None:
        # Update user data with bank and account number
        user_data[user_index]['bank'] = bank
        user_data[user_index]['account_number'] = account_number

        # Write updated user data to the JSON file
        with open(file_path, 'w') as file:
            json.dump(user_data, file, indent=2)

        return True
    else:
        return False
