import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не задана!")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для покупки фото.")

@router.message(Command("buy_photo"))
async def buy_photo(message: types.Message):
    await message.answer("Выбери фото для покупки.")

async def main():
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
