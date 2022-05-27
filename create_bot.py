from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5346682389:AAEDzrZiNRgIWY1d1ZGXAFn_6MqJnnwDub4'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
