from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup(row_width=1)
add_new = InlineKeyboardButton(text='Добавить новую позицю', callback_data='add_new')
edit_old = InlineKeyboardButton(text='Изменить/удалить позицию', callback_data='edit_old')
finish = InlineKeyboardButton(text='Завершить', callback_data='finish')
markup.add(add_new, edit_old, finish)

markup_add = InlineKeyboardMarkup(row_width=1)
back = InlineKeyboardButton(text='Назад', callback_data='back')
markup_add.add(back)