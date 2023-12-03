from interface.api import DataItem

def calculator(data_user:DataItem):
    sorted_data = sorted(data_user, key=lambda x: x.money, reverse=True)
    total_money = sum(entry.money for entry in data_user)
    if total_money != 0:
        return
    else:
        return sorted_data
        for user in sorted_data:
            if user["money"] < 0:
                print(f"Thằng {user['id']} đang nợ {user['money']}")
            elif user["money"] > 0:
                print(f"Thằng {user['id']} được từng ni tiền {user['money']}")
            else:
                print(f"Thằng ni hoà vốn!")