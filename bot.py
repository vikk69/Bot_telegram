import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Загружаем токен из переменных среды (добавишь на Railway)
TOKEN = os.getenv("BOT_TOKEN")

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для продажи фото. Напиши /buy_photo, чтобы купить.")

# Команда /buy_photo
@dp.message_handler(commands=['buy_photo'])
async def buy_photo(message: types.Message):
    await message.answer("Выбери фото для покупки:\n1️⃣ Фото 1 - 10 USDT\n2️⃣ Фото 2 - 15 USDT\n\nОплата: [TON Payments](https://t.me/tonbank_bot)")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
