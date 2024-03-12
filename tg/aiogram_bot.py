import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)  # bot yaratish class
dp = Dispatcher(bot)  # Boshqarish uchun dastup


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_username = message.from_user.username
    await message.reply(f"Hi @{user_username}")


if __name__ == "main":
    executor.start_polling(dp, skip_updates=True)
