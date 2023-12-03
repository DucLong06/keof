import os
from telegram import Bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Xin chào tôi là bot tính tiền kèo cầu lông.\n"
        "Để đăng ký tài khoản người chơi sử dụng cú pháp /reg <email>. \n",
        "Nếu bạn là chủ nợ muốn nhận được tiền sử dụng cú pháp và /bank <tên ngân hàng>|<stk>. \n"
        )



async def register(update: Update, context: CallbackContext):
    pass


def main() -> None:
    bot_token = os.getenv("TOKEN")
    try:
        print("bot is running!")
        application = ApplicationBuilder().token(bot_token).build()
        start_handler = CommandHandler('start', start)
        register_handler = CommandHandler('reg', register())
        
        application.add_handler(start_handler)
        application.add_handler(register_handler)
        application.run_polling()
    except Exception as e:
        print(f"bug {str(e)}")
        
        
async def notify(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id, message)
