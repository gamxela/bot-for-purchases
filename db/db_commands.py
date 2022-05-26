import sqlite3

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


async def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    await cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                         (user_id, user_name, user_surname, username))
    await conn.commit()


async def add_item(user_id: int, product: str, count: int, status: int):
    await cursor.execute('INSERT INTO list_p (user_id, product, count, status) VALUES (?, ?, ?, ?)',
                         (user_id, product, count, status))
    await conn.commit()

# def delete_item(self, item_text):
#     stmt = "DELETE FROM items WHERE description = (?)"
#     args = (item_text, )
#     self.conn.execute(stmt, args)
#     self.conn.commit()

# def get_items(self):
#     stmt = "SELECT description FROM items"
#     return [x[0] for x in self.conn.execute(stmt)]
