from aiogram import types
from create_bot import dp, bot
from db import db_commands
from handlers.keyboard import markup, markup_add
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMadd(StatesGroup):
    waiting_for_product = State()
    waiting_for_delproduct = State()  # Задаем состояние


@dp.callback_query_handler(text='add_new', state=None)
async def process_callback_add(callback: types.CallbackQuery):

    await callback.answer()
    await FSMadd.waiting_for_product.set()  # Устанавливаем состояние
    await bot.send_message(callback.message.chat.id, 'Отправь имя продукта, для добавления в список.'
                                                     'Пожалуйста используй такой формат:\n'
                                                     'Мука - 2 кг')
    # await bot.edit_message_text('Пришли мне продукты для твоего списка', callback.message.chat.id, callback.message.message_id, reply_markup=markup_add)


@dp.message_handler(state=FSMadd.waiting_for_product)  # Принимаем состояние
async def product_add(message: types.Message, state: FSMContext):

    async with state.proxy() as data:  # Устанавливаем состояние ожидания
        data['waiting_for_product'] = message.text
    # await message.answer(f"Вы написали - {data['waiting_for_product'].split('-')[0]}\n"
    #                      f"Количество - {data['waiting_for_product'].split('-')[1]}")
    await bot.send_message(message.chat.id, 'Список успешно обновлен', reply_markup=markup_add)
    user_id = message.from_user.id
    product = data['waiting_for_product'].split('-')[0].strip()
    count = data['waiting_for_product'].split('-')[1].strip()
    status = 1
    db_commands.add_item(user_id=user_id, product=product,
                         count=count, status=status)
    await state.finish()  # Выключаем состояние


@dp.callback_query_handler(text='edit_old', state=None)
async def process_callback_edit(callback: types.CallbackQuery):

    await callback.answer()
    await FSMadd.waiting_for_delproduct.set()  # Устанавливаем состояние
    await bot.send_message(callback.message.chat.id, 'Отправь имя продукта, которое хотел бы удалить из списка:')
    # await bot.edit_message_text('Выбери что ты хочешь изменить или удалить', callback.message.chat.id, callback.message.message_id, reply_markup=markup_add)
    

@dp.message_handler(state=FSMadd.waiting_for_delproduct)  # Принимаем состояние
async def product_del(message: types.Message, state: FSMContext):

    async with state.proxy() as data:  # Устанавливаем состояние ожидания
        data['waiting_for_delproduct'] = message.text
    # await message.answer(f"Вы написали - {data['waiting_for_delproduct']}")
    await bot.send_message(message.chat.id, 'Список успешно обновлен', reply_markup=markup_add)
    user_id = message.from_user.id
    product = data['waiting_for_delproduct']
    db_commands.delete_item(user_id=user_id, product=product)
    await state.finish()  # Выключаем состояние


@dp.callback_query_handler(text='back')
async def process_callback_back(callback: types.CallbackQuery):

    await callback.answer()
    await bot.edit_message_text('Приступим к редактированию твоего списка', callback.message.chat.id, callback.message.message_id, reply_markup=markup)


@dp.callback_query_handler(text="finish")
async def process_callback_finish(callback: types.CallbackQuery):

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)

