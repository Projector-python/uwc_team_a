import sqlite3


class DataBase ():
    def __init__(self, filename: str = 'uwc_database.db'):
        self.connection = sqlite3.connect(filename, check_same_thread=False)

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

        cursor.execute("SELECT * FROM users WHERE is_admin is True")
        admin_list = cursor.fetchall()

        if len(admin_list) == 0:
            print(cursor.fetchall())
        else:
            for admin in admin_list:
                print(admin)

    def remove_admin_from_db(self, telegram_id: int):
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM users WHERE telegram_id = ?",
                       (telegram_id,))

        self.connection.commit()

    def is_admin(self, telegram_id: int) -> bool:
        cursor = self.connection.cursor()

        cursor.execute("SELECT telegram_id FROM users WHERE is_admin is True")

        admin_list = set([x[0] for x in cursor.fetchall()])

        if telegram_id in admin_list:
            return True
        else:
            return False

    def add_user(self, *args, **kwargs):
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


db = DataBase()
