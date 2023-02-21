import sqlite3
from constants import database


class DataBase ():
    def __init__(self, filename: str = 'uwc_database.db'):
        self.connection = sqlite3.connect(connection, check_same_thread=False)

    def create_table_users(self):
        self.connection.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                telegram_id INT NOT NULL,
                name VARCHAR(50) NOT NULL,
                is_admin BOOL
            );
        """)

        self.connection.commit()

    def add_admin_to_db(self, *args):
        self.connection.execute("""
            INSERT INTO users (telegram_id, name, is_admin) VALUES (?, ?, True)
        """, args)
        self.connection.commit()

    def show_admin_from_db(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM users WHERE is_admin == True")
        admin_list = cursor.fetchall()

        if len(admin_list) == 0:
            print(cursor.fetchall())
        else:
            for admin in admin_list:
                print(admin)

    def remove_admin_from_db(self, admin_id: int):
        cursor = self.connection.cursor()

        cursor.execute(f"DELETE FROM users WHERE telegram_id == {admin_id}")

        self.connection.commit()

    def is_admin(self, admin_id: int) -> bool:
        cursor = self.connection.cursor()

        cursor.execute("SELECT telegram_id FROM users")
        temp = cursor.fetchall()

        admin_list = set([x[0] for x in temp])

        if admin_id in admin_list:
            return True
        else:
            return False

    def add_user_id(self, *args, **kwargs):
        pass

    def get_telegram_id_list(self) -> list:
        cursor = self.connection.cursor()

        cursor.execute("SELECT telegram_id FROM users")
        temp = cursor.fetchall()

        user_list = set([x[0] for x in temp])

        return user_list

    def show_all_users(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM users")
        user_list = cursor.fetchall()

        if len(user_list) == 0:
            print(cursor.fetchall())
        else:
            for user in user_list:
                print(user)


db = DataBase('uwc_database.db')
