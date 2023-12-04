import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
from utils import read_data_json, update_user_data, write_data_json
import dotenv
import logzero
from logzero import logger

# set up log
logzero.logfile("log/bot_tele.log", maxBytes=1e6, backupCount=3)


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Xin chào tôi là bot tính tiền kèo cầu lông.\n"
        "Để đăng ký tài khoản người chơi sử dụng cú pháp /reg <email>. \n"
        "Để đăng ký tài khoản nhận tiền sử dụng cú pháp và /bank <tên ngân hàng>|<stk>. \n"
    )


async def register_bank(update: Update, context: CallbackContext):
    # Get user input
    user_id = update.message.from_user.id
    bank_info = context.args[0] if context.args else None

    try:
        # Check if bank information is provided
        if not bank_info or '|' not in bank_info:
            await update.message.reply_text(
                'Làm ơn cung cấp thông tin ngân hàng ví dụ /bank techcombank|LongLoe')
            return

        # Split bank information into bank name and account number
        bank_name, account_number = bank_info.split('|', 1)

        # Update user data with bank information
        success = update_user_data(
            "db/User.json", str(user_id), bank_name, account_number)

        if success:
            await update.message.reply_text(
                f'Tài khoản ngân hàng của bạn đã được cập nhật:\nNgân hàng: {bank_name}\nSố tài khoản: {account_number}')
        else:
            await update.message.reply_text('Người chơi chưa đăng ký tài khoản hoặc có lỗi xảy ra.')

    except Exception as e:
        logger.error(f"Error in register_bank: {str(e)}")


async def register(update: Update, context: CallbackContext):
    # Get user input
    user_id = update.message.from_user.id
    email = context.args[0] if context.args else None

    try:
        # Check if email is provided
        if not email:
            await update.message.reply_text(
                'Làm ơn cung cấp email ví dụ /reg longdaika@gmail.com')
            return

        # Check if the user ID or email already exists in the JSON file
        users = read_data_json("db/User.json")
        existing_user = next((user for user in users if user.get(
            'id') == user_id or user.get('email') == email), None)

        if existing_user:
            existing_email = existing_user.get('email', '')
            await update.message.reply_text(f'Email đã tồn tại. Không được phép đăng ký. Email đã đăng ký: {existing_email}')
            return

        # Prepare user data
        user_data = {'id': user_id, 'email': email}

        # Write user data to the JSON file
        write_data_json("db/User.json", [user_data])

        await update.message.reply_text(
            f'Tài khoản của bạn được đăng ký thành công với email: {email}')

    except Exception as e:
        logger.error(f"Error in register: {str(e)}")


def main() -> None:
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    bot_token = os.getenv("TOKEN")
    try:
        logger.info("Bot is running")
        application = ApplicationBuilder().token(bot_token).build()
        start_handler = CommandHandler('start', start)
        register_handler = CommandHandler('reg', register)
        register_bank_handler = CommandHandler('bank', register_bank)

        application.add_handler(start_handler)
        application.add_handler(register_bank_handler)
        application.add_handler(register_handler)
        application.run_polling()

    except Exception as e:
        logger.error(f"Exception in main: {str(e)}")


if __name__ == '__main__':
    main()
