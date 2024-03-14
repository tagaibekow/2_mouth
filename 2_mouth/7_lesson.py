# CУБД - Система Управления Базой Данных
# БД- база данных
# CRUD - Create, Read, Update, Delete

# DB - data base

import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection 

create_connection('school.db')

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

# execute - Отправляет запрос в база данных
# cursor - Посредник между нашим кодом и база данных(sqlite3)
    
def create_student(conn, student: tuple):
    sql = """ INSERT INTO students
    (fullname, age, hobby, birthday, mark, is_passed)
    VALUES(?, ?, ?, ?, ?, ?);"""
    cursor = conn.cursor()
    cursor.execute(sql,student)
    conn.commit()
    
# str - TEXT, VARCHAR(100)
# int - INTEGER
# bool - BOOLEAN
# float - DOUBLE




# # IF NOT EXISTS = создать таблицу если такой не существует
# # AUTOINCREMENT = сам сгенерирует айди
# # VARCHAR = текст с ограниченной длиной(str)
# # NOT NULL = обязательное поле
# # DOUBLE = float
# # TEXT = текст без ограничений(str)
# # DEFAULT NULL = необязательное поле

    
#  PRIMARY KEY - УНИКАЛЬНЫЙ КЛЮЧ что бы не было дубликатов
# IF NOT EXISTS - условие чтобы бд два раза не создавалась и вне выдавал ошибку

sql_create_table = """
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (100) NOT NULL,
age INTEGER NOT NULL,
hobby TEXT NULL,
birthday DATE NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
is_passed BOOLEAN DEFAULT FALSE
);"""

connection = create_connection('school.db')
if connection:
    print('успешное подключение')
    create_table(connection, sql_create_table)
    create_student(connection, ('Tagaibekov Daiyrbek', 15, 'programist', "23-05-2009", 100.00, True))