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

    def add_admin_to_db(self, telegram_id: int, name: str):
        self.connection.execute("""
            INSERT INTO users (telegram_id, name, is_admin) VALUES (?, ?, True)
        """, (telegram_id, name))
        self.connection.commit()

    def remove_admin_from_db(self, telegram_id: int):
        cursor = self.connection.cursor()

        cursor.execute("""
            DELETE FROM users WHERE telegram_id = ?
            """, (telegram_id,))

        self.connection.commit()

    def show_admin_from_db(self):
        pass

    def is_admin(self, telegram_id: int) -> bool:
        cursor = self.connection.cursor()

        cursor.execute(f"""
            SELECT EXISTS(SELECT * FROM users
            WHERE is_admin = true
            AND telegram_id = {telegram_id})
            """)

        return cursor.fetchone()

    def add_user(self, *args, **kwargs):
        pass

    def get_telegram_id_list(self) -> list:
        cursor = self.connection.cursor()

        cursor.execute("SELECT telegram_id FROM users")
        temp = cursor.fetchall()

        user_list = set([x[0] for x in temp])

        return user_list

    def show_all_users(self):
        pass


db = DataBase()
