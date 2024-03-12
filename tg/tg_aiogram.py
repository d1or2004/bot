import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from main import Database

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)
    check_query = f""" SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if (Database.connetc(check_query, "select")) >= 1:
        await message.reply(f"Hi {message.chat.id}")
    else:
        print(f"{first_name} start bot")
        query = f""" INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}','{last_name}','{username}','{chat_id}')"""
        print(f"{username} {Database.connetc(query, 'insert')} database ")
        await message.reply(f"Hi {message.chat.id}")

#
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    query_select = "SELECT * FROM users"
    data = Database.connetc(query_select,"select")
    await message.reply(data)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
