import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection('hw.db')

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

    
def create_products(conn, product: tuple):
    sql = """ INSERT INTO products
    (product_title, price, quantity)
    VALUES(?, ?, ?);"""
    cursor = conn.cursor()
    cursor.execute(sql,product)
    conn.commit()
    

sql_create_table="""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (100) NOT NULL,
price DOUBLE (6, 3) NOT NULL DEFAULT 0.0,
quantity  INTEGER NOT NULL DEFAULT 0);"""

connection = create_connection('hw.db')
if connection:
    print('успешное подключение')
    create_table(connection, sql_create_table)
    create_products(connection, ('APPLE', 100, '3КГ'))