import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, Router

# Загружаем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)  # Добавляем router в диспетчер

# Команда /start
@router.message(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для продажи фото.")

# Команда /buy_photo
@router.message(commands=['buy_photo'])
async def buy_photo(message: types.Message):
    await message.answer("Выбери фото для покупки.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
