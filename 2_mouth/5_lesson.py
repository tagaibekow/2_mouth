# import time

# print("Код запуститься через 1 секунд")

# time.sleep(1)

# print("HELLO WORLD!")

# while True:
#     print("") 

"""
Модули - все файлы с расширением .py
"""

"""
Кастомные : Модули которые мы создаем сами ( lesson_1.py )
"""

"""
Встроенные: Модули которые встроены в язык python ( random, time, mathdatetime )
"""

# import time

# print("Код запуститься через 5 сек")

# time.sleep(5)

# print("Hello World!")

# start = time.time()

# n = 0

# while n < 7:
#     n += 1
#     # time.sleep(0.5)
#     print("Loading...")

# end = time.time()

# result = end - start
# print(result)

"""
Внешние : Модули которые нужно скачивать для исполльзования ( библиотеки или фреймворки )
"""

# pip - Пакетный менеджер python

from termcolor import cprint

print("Hello World!")

cprint("Hello World!", "red", "on_green")


"""
python -m venv venv

./venv/Scripts/activate

pip install 

pip freeze

pip uninstall

"""


import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS banks(
               id INTEGER PRIMARY KEY ,
               fullname VARCHAR (100) NOT NULL,
               age INTEGER NOT NULL,
               address VARCHAR (100) NOT NULL,
               email VARCHAR (100) NOT NULL,
               balance INTEGER NOT NULL DEFAULT 0);
               """)

class Bank:
    def __init__(self):
        self.fullname = None
        self.age = 0
        self.address = None
        self.email = None

    def register(self, fullname,  age, address, email):
        self.name = fullname
        self.age = age
        self.address = address
        self.email = email
        cursor.execute(f"""
                        INSERT INTO banks (fullname, age, address, email)
                       VALUES ('{fullname}',  0,' {address}',' {email}');""")
        connect.commit()

    def plus_money(self, amount):
        cursor.execute(f"UPDATE banks SET balance = balance + {amount} WHERE email = {self.email}")
        connect.commit()
        self.plus_money += amount

    def minus_money(self, amount):
        cursor.execute(f"UPDATE banks SET balance = balance - {amount} WHERE email = '{self.email}' ")
        connect.commit()
        self.plus_money -= amount
        
    def __str__(self):
        return f"Ваш текущий баланс {self.balance}"

    def main(self):
        while True:
            print("Выберите команду: ")
            print("1-Регистрация, 2-Пополнение, 3-Вывести деньги, 4-Выйти")
            command = int(input("Выберите действие: "))
            if command ==1:
                fullname = input("Введите ваше имя: ")
                age = input("Введите ваш возраст: ")
                address = input('Введите ваш адрес: ')
                email = input('Введите ваш email: ')
                print('Успешное регистрация!!!')
                self.register(fullname, age, address, email)

            elif command == 2:
                if self.email:
                    print('Пополните поле!!!')
                    
                    amount = int(input("Введите сумму: "))
                    
                else:
                    print("Сделайте регистрацию")
                self.plus_money(amount)

            elif command == 3:
                if self.email:
                    print('Вывести средства')
                    amount = int(input("Введите сумму: "))
                    self.minus_money(amount)
                    
            elif command == 4:
                break
            else:
                print("1-Регистрация, 2-Пополнение, 3-Вывести деньги, 4-Выйти")
                command = int(input("Выберите действие: "))

bank = Bank()
bank.main() 