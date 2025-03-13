from aiogram import Bot, Dispatcher
import asyncio
import logging
import os

# Загружаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота
bot = Bot(token=TOKEN)

# Создаём диспетчер
dp = Dispatcher()

# Регистрируем бота в диспетчере
dp["bot"] = bot

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer("Привет! Я бот для продажи фото.")

# Команда /buy_photo
@dp.message_handler(commands=['buy_photo'])
async def buy_photo(message):
    await message.answer("Выбери фото для покупки.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
