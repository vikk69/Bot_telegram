import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types

# Загружаем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для покупки фото.")

# Команда /buy_photo
@dp.message_handler(commands=['buy_photo'])
async def buy_photo(message: types.Message):
    await message.answer("Выбери фото для покупки.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
