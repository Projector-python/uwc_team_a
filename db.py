import sqlite3

# connection = sqlite3.connect('uwc_database.db')

# connection.execute("""
#     CREATE TABLE admins (
#         admin_id INT NOT NULL,
#         name VARCHAR(50) NOT NULL
#     );
# """)


# connection.execute("""
#     CREATE TABLE all_users (
#         user_id INT NOT NULL
#     );
# """)

# cursor = connection.cursor()

# connection.commit()
# connection.close()


def add_admin_to_db(*args):
    connection = sqlite3.connect('uwc_database.db')
    connection.execute("""
        INSERT INTO admins VALUES (?, ?)
    """, args)
    connection.commit()
    connection.close()


def remove_admin_from_db(admin_id: int):
    connection = sqlite3.connect('uwc_database.db')
    cursor = connection.cursor()
    
    cursor.execute(f"DELETE FROM admins WHERE admin_id == {admin_id}")
    
    connection.commit()
    connection.close()


def show_admin_from_db():
    connection = sqlite3.connect('uwc_database.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM admins")
    admin_list = cursor.fetchall()

    if len(admin_list) == 0:
        print(cursor.fetchall())
    else:    
        for admin in admin_list:
            print(admin)
    
    connection.close()


def is_admin(admin_id: int) -> bool:
    connection = sqlite3.connect('uwc_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT admin_id FROM admins")
    temp = cursor.fetchall()

    admin_list = set([x[0] for x in temp])

    if admin_id in admin_list:
        return True


def add_user_id(user_id: int):
    connection = sqlite3.connect('uwc_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT user_id FROM all_users")
    temp = cursor.fetchall()

    user_list = set([x[0] for x in temp])

    if user_id not in user_list:
        connection.execute(f"INSERT INTO all_users VALUES ({user_id})")
    
    connection.commit()
    connection.close()


def get_user_id_list() -> list:
    connection = sqlite3.connect('uwc_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT user_id FROM all_users")
    temp = cursor.fetchall()

    user_list = set([x[0] for x in temp])

    connection.close()
    return user_list


def show_all_users_id():
    connection = sqlite3.connect('uwc_database.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM all_users")
    user_list = cursor.fetchall()

    if len(user_list) == 0:
        print(cursor.fetchall())
    else:
        for user in user_list:
            print(user)

    connection.close()
