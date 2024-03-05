numl = int (input ("Введите - первое число:") )
num2= int (input ("Введите второе число:  "))  
print (f"Результат после - сложения: {numl+num2}")

import random
randon = random. randint (1,5)
numl = int (input ("Введите число от - 1 до 5: "))
if numl ==randon:
 print (f"Вы выиграли!! Бот выиграл: {randon}")
else:
     print (f"Вы проиграли!! Бот выиграл: {randon}")

def result(num1,num2):
   print(f"Результат после сложение: {num1+num2}")
result(5,6)

def rent():
   random = random.randint(1,5)
   numl = int (input ("Введите число от - 1 до 5: "))
   if numl ==random:
    print (f"Вы выиграли!! Бот выиграл: {random}")
   else:
     print (f"Вы проиграли!! Бот выиграл: {random}")
rent()

def register(name,age,phone):
    if age <= 18:
        print("Добро пожаловать в наш замечательный мир:")
        print(f"{name} {age}, {phone}")
    else:
        print("Доступ запрещен")
register("Хожиакбар",18,"0990530084")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"Результат после сложения: {num1+num2}")


# import random

# randon = random.randint(1,5)
# num1 = int(input("Введите число от 1 до 5: "))
# if num1 ==randon:
#     print(f"Вы выиграли!! Бот выиграл: {randon}")
# else:
#     print(f"Вы проиграли!! Бот выиграл: {randon}")


# # def hello():
# #     print("Hello world")

# def result(num1,num2):
#     print(f"Красивый результат после сложения: {num1+num2}")
# result(12,3)

# def result1():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(f"Результат после сложения: {num1+num2}")
# result1

# ###############################################################
# import random

# def rungame(num):
#     randon = random.randint(1,5)
#     if num ==randon:
#         print(f"Вы выиграли!! Бот выиграл: {randon}")
#     else:
#         print(f"Вы проиграли!! Бот выиграл: {randon}")
# rungame(2)

# def rungame2():
#     randon = random.randint(1,5)
#     num1 = int(input("Введите число от 1 до 5: "))
#     if num1 ==randon:
#         print(f"Вы выиграли!! Бот выиграл: {randon}")
#     else:
#         print(f"Вы проиграли!! Бот выиграл: {randon}")
# rungame2()


#Создайте функцию register() он будет запращивать 3 значения(name,age,phone). Вы должны сделать проверку на возраст, если пользователю больше 18 лет. Вы должны вывести текст "Добро пожаловать в наш замечательный мир." и так же "Имя: Geeks, Телефонный номер:  0558000350, возраст: 19"

# Если ему нет 18 лет, должны вывести "Доступ запрещен!!!"

# def numbers(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
#     print(num1,num2,num3)
    
# numbers(1,2,3,4,5,6,7,8,9,10)

# def nums(*num1):
#     print(num1)
# nums(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)


# def dicts(**users):
#     print(users)

# dicts(name = "Nurbolot", age = 15,city = "Osh", hobby = "it")


import random 

def game(num):
    ran = random.randint(1,5)
    if num == ran:
        print(f" Вы выиграли. Бот выбрал: {ran}")
    else:
        print(f" Вы проиграли. Бот выбрал: {ran}")
        
def menu():
    while True:
        print("1 - Играть, 2 - узнать информацию!!!")
        shag = input("Введите свой выбор: ")
        if shag == "1":
            num1 = int(input("Введите число от 1 до 5: "))
            game(num1)
            

def register(name,age,phone):
    if age >= 18:
        print("Добро пожаловать в наш замечательный мир!!!")
        print(f" Имя: {name}, возраст: {age}, телефонный номер: {phone}")
        menu()
    else:
        print("Доступ запрещен")

name = input("Введите имя: ")
age = int(input("Введите возраст: "))
phone = input("Введите телефонный номер: ")
register(name,age,phone)