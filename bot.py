import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router, types

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для покупки фото.")

@router.message(commands=['buy_photo'])
async def buy_photo(message: types.Message):
    await message.answer("Выбери фото для покупки.")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
