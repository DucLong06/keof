import os
import dotenv
from interface.api import DataItem
from telegram import Bot

data_admin = "STK: longloe\nNgân hàng: Techcombank"


async def calculator(data_user: DataItem, current_date):
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    bot_token = os.getenv("TOKEN")

    bot = Bot(token=bot_token)
    sorted_data = sorted(data_user, key=lambda x: x.money, reverse=True)

    for user in sorted_data:
        if user.money < 0:
            await bot.send_message(user.id, f"Ngày:{current_date}:\nBạn đang nợ: {user.money * 10 * -1}.000 VNĐ\nVui lòng chuyển khoản cho admin với thông tin\n{data_admin}")
        elif user.money > 0:
            await bot.send_message(user.id, f"Ngày:{current_date}:\nBạn thằng kèo được: {user.money * 10}.000 VNĐ")
        else:
            await bot.send_message(user.id, f"Ngày:{current_date}:\nNay bạn đi chơi vui vẻ")
