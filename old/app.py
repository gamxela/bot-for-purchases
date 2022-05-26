import telebot
from telebot import types
import sqlite3

TOKEN = "5346682389:AAEDzrZiNRgIWY1d1ZGXAFn_6MqJnnwDub4"
bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

def on_startup(_):
    print('Бот запущен!')

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()

def add_item(user_id: int, product: str, count: int, status: int):
        cursor.execute('INSERT INTO list_p (user_id, product, count, status) VALUES (?, ?, ?, ?)',
                       (user_id, product, count, status))
        conn.commit()


def get_message_product(message):
    
    return message.text


# def delete_item(self, item_text):
#     stmt = "DELETE FROM items WHERE description = (?)"
#     args = (item_text, )
#     self.conn.execute(stmt, args)
#     self.conn.commit()

# def get_items(self):
#     stmt = "SELECT description FROM items"
#     return [x[0] for x in self.conn.execute(stmt)]


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    
    info = cursor.execute('SELECT * FROM test WHERE user_id=?', (message.from_user.id, ))
    if info.fetchone() is None: 
        bot.send_message(message.from_user.id,
                        'Привет! Выберив меню /edit, чтобы создать свой первый список покупок')
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        db_table_val(user_id=us_id, user_name=us_name,
                    user_surname=us_sname, username=username)
    else:
        bot.send_message(message.from_user.id,
                        'С возвращением! Используй меню, чтобы узнать или изменить свой список')
        

@bot.message_handler(commands=['edit'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    add_new = types.InlineKeyboardButton(text='Добавить новую позицю', callback_data = 'add')
    edit_old = types.InlineKeyboardButton(text='Изменить/удалить позицию', callback_data = 'edit')
    finish = types.InlineKeyboardButton(text='Завершить', callback_data = 'finish')

    markup.add(add_new, edit_old, finish)
    bot.send_message(message.chat.id,'Приступим к редактированию твоего списка', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:'add')
def answer(call):
    bot.answer_callback_query(callback_query_id=call.id)
    # if call.data == 'add':
    bot.send_message(call.message.chat.id,'Пришли мне продукты для твоего списка')
    
    
    call.answer('Добавлено успешно')
    # elif call.data == 'edit':
    #     pass
    # elif call.data == 'help':
    #     pass
    # elif call.data == 'settings':
    #     pass


def add_new(message):
    us_id = call.message.from_user.id
    count = 1
    status = 1
    product = register_next_step_handler(message)
    add_item(user_id=us_id, product=product, count=count, status=status)
    call.answer('Добавлено успешно')
    
    message.answer('Добавлено успешно')

bot.polling(none_stop=True)
