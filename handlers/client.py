from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import dispatcher
from create_bot import dp, bot
from db import db_commands


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
        await db_commands.db_table_val(user_id=us_id, user_name=us_name,
                                       user_surname=us_sname, username=username)
    else:
        await bot.send_message(message.chat.id,
                               'С возвращением! Используй меню, чтобы узнать или изменить свой список')


markup = InlineKeyboardMarkup(row_width=1)
add_new = InlineKeyboardButton(text='Добавить новую позицю', callback_data='add_new')
edit_old = InlineKeyboardButton(text='Изменить/удалить позицию', callback_data='edit')
finish = InlineKeyboardButton(text='Завершить', callback_data='finish')
markup.add(add_new, edit_old, finish)


# @dp.message_handler(commands=['edit'])
async def edit_list(message: types.Message):

    await bot.send_message(message.chat.id, 'Приступим к редактированию твоего списка', reply_markup=markup)


# @dp.callback_query_handler(text='add_new')
async def process_callback_add(callback: types.CallbackQuery):

    await callback.answer(cache_time=60)
    markup_add = InlineKeyboardMarkup(row_width=1)
    finish = InlineKeyboardButton(text='Назад', callback_data='back')
    markup_add.add(finish)
    await bot.edit_message_reply_markup(callback.message.chat.id,'Пришли мне продукты для твоего списка', reply_markup=markup_add)

    # await bot.answer_callback_query(callback_query_id=callback.id)
    # await bot.send_message(call.from_user.id,'Пришли мне продукты для твоего списка')
    # await callback_query.answer('Добавлено успешно')


# @dp.callback_query_handler(text='back')
async def process_callback_back(callback: types.CallbackQuery):

    await bot.edit_message_reply_markup(callback.message.chat.id, 'Приступим к редактированию твоего списка', reply_markup=markup)


def register_handlers_client(dp: dispatcher):

    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(edit_list, commands=['edit'])
    dp.register_message_handler(process_callback_add, text='add_new')
    dp.register_message_handler(process_callback_back, text='back')
