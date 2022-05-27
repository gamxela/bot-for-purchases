from aiogram import types
from aiogram.dispatcher import dispatcher
from create_bot import dp, bot
from db import db_commands
from handlers.keyboard import markup


# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    info = db_commands.cursor.execute(
        'SELECT * FROM test WHERE user_id=?', (message.from_user.id, ))
    if info.fetchone() is None:
        await bot.send_message(message.chat.id,
                               'Привет! Выбери в меню /edit, чтобы создать свой первый список покупок')
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        db_commands.db_table_val(user_id=us_id, user_name=us_name,
                                       user_surname=us_sname, username=username)
    else:
        await bot.send_message(message.chat.id,
                               'С возвращением! Используй меню, чтобы узнать или изменить свой список')


# @dp.message_handler(commands=['settings'])
async def send_settings(message: types.Message):

    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, 'Здесь будут настройки - например, синхронезация с другим списком')


# @dp.message_handler(commands=['list'])
async def show_list(message: types.Message):

    # await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, 'Вот твой список:\n'+db_commands.get_items(message.from_user.id))


# @dp.message_handler(commands=['edit'])
async def edit_list(message: types.Message):

    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, 'Приступим к редактированию твоего списка', reply_markup=markup)


def register_handlers_client(dp: dispatcher):

    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(edit_list, commands=['edit'])
    dp.register_message_handler(send_settings, commands=['settings'])
    dp.register_message_handler(show_list, commands=['list'])

