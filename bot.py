from aiogram import Bot, Dispatcher
import asyncio
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp["bot"] = bot

@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer("Привет! Я бот для продажи фото.")

@dp.message_handler(commands=['buy_photo'])
async def buy_photo(message):
    await message.answer("Выбери фото для покупки.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
