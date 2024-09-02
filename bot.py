# 1. Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher # две основные сущности в библиотеке
from aiogram.types import Message # ловим все обновления этого типа
from aiogram.filters.command import Command # обработка команд /start, /help и другие

# 2. Импорт функции транскрипции

from transcription_func import transcription

# 3. Инициализация объектов

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,
    filename='bot_logs.log',
    format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%H:%M:%S'
    )

# 4. Обработка команды start

@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Введи ФИО полностью для получения транскрипции!'
    logging.info(f'{user_name} с {user_id} запустил бота!')
    await bot.send_message(chat_id=user_id, text=text)

# 5. Обработка всех сообщений

@dp.message()
async def send_tranc_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} с {user_id}: {text}')
    await message.answer(text=transcription(text))

# 6. Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)
