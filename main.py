import logging

from handlers import client, commands
from aiogram import executor
from create_bot import dp

# Configure logging
# logging.basicConfig(filename='filename.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG)


async def on_startup(_):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Бот вышел в онлайн%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


commands.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
