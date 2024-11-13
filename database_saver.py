# from sqlite3 import connect

# con = connect("users.db")
# cursor = con.cursor()

# #sorov_table
# #id primary key AUTOINCEMENT INTEGER
# #name TEXT NULL
# #time TEXT NULL
# #status TEXT NULL 
# #user_id
# #sabab TEXT NULL


# #history_table
# #id primary key AUTOINCEMENT INTEGER
# #user_id INTEGER
# #sorov_id INTEGER
# #status TEXT NULL
# def insert_sorov_table(name,time,user_group,status,user_id,sabab):
#     cursor.execute("""CREATE TABLE IF NOT EXISTS sorov_table (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NULL,
#     time TEXT NULL,
#     user_group TEXT NULL ,
#     status TEXT NULL,
#     user_id INTEGER,
#     user_group INTEGER,
#     sabab TEXT NULL
# )""")

# # cursor.execute("""CREATE TABLE IF NOT EXISTS history_table (
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     name TEXT NULL,
# #     time TEXT NULL,
# #     group TEXT NULL,
# #     status TEXT NULL,
# #     user_id INTEGER,
# #     sabab TEXT NULL
# # )""")

# # con.commit()
import sqlite3



def create_table():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    
    # Создание таблицы sorov_table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sorov_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NULL,
            time TEXT NULL,
            guruxlar TEXT NULL,
            status TEXT NULL DEFAULT "Ожидание ответа",
            filial TEXT NULL,
            user_id INTEGER NOT NULL,
            sabab TEXT NULL
        )
    ''')
    
    # Создание таблицы history_sorov
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history_sorov (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NULL,
            time TEXT NULL,
            guruxlar TEXT NULL,
            status TEXT NULL,
            filial TEXT NULL,
            user_id INTEGER NOT NULL,
            sabab TEXT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Call to ensure table is created
create_table()

# Function to insert new request into database
def save_request_sorov_table(user_id, name, time, guruxlar, filial, sabab):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sorov_table (user_id, name, time, guruxlar, filial, sabab)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, name, time, guruxlar, filial, sabab))
    conn.commit()
    conn.close()

# Function to update the status
def update_status(user_id, new_status):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE sorov_table
        SET status = ?
        WHERE user_id = ?
    ''', (new_status, user_id))
    conn.commit()
    conn.close()

# Function to save request to history_sorov
def save_request_to_history(user_id):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Получаем данные из sorov_table для указанного user_id
    cursor.execute('''
        SELECT name, time, guruxlar, status, filial, sabab
        FROM sorov_table
        WHERE user_id = ?
    ''', (user_id,))
    request = cursor.fetchone()

    if request:
        name, time, guruxlar, status, filial, sabab = request
        
        # Сохраняем в history_sorov
        cursor.execute('''
            INSERT INTO history_sorov (user_id, name, time, guruxlar, status, filial, sabab)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, name, time, guruxlar, status, filial, sabab))

        # Удаляем запись из sorov_table
        cursor.execute('DELETE FROM sorov_table WHERE user_id = ?', (user_id,))
    
    conn.commit()
    conn.close()
