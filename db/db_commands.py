import sqlite3

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                         (user_id, user_name, user_surname, username))
    conn.commit()


def add_item(user_id: int, product: str, count: int, status: int):
    cursor.execute('INSERT INTO list_p (user_id, product, count, status) VALUES (?, ?, ?, ?)',
                         (user_id, product, count, status))
    conn.commit()


def get_items(user_id: int):
    info = cursor.execute('SELECT * FROM list_p WHERE (user_id, status)=(?, ?)', (user_id, 1))
    info = info.fetchall()
    message_str = ""
    for i in info:
        if i[3] == None:
            message_str += f"{i[2]}\n"
        else:
            message_str += f"{i[2]} {i[3]}\n"
    return message_str

def delete_item(user_id: int, product: str):
    cursor.execute('DELETE FROM list_p WHERE (user_id, product)=(?, ?)', (user_id, product))
    conn.commit()

# def get_items(self):
#     stmt = "SELECT description FROM items"
#     return [x[0] for x in self.conn.execute(stmt)]
