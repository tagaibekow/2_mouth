# users = [2,"hello", True,[1,2,3,4],2.3]
# print(users)

# numbers = [1,2,3,4,1,2,3,4]
# print(numbers)
# #           0           1           2           3
# users = ["Geeks", "Kutbuhanbek", "Nurbek", "Aibek"]
# print(users[1:4])

# Методы добавление в список

users = ["Geeks", "Kutbuhanbek", "Nurbek", "Aibek"]
print(users)
users.append("Beksultan")       # Для добавления в конец списка
print(users)
users.insert(1, "Antonbek")     # Для добавления по индексу
print(users)

userss = ["Aslanbek","Hodjiakbarbek"]
users.extend(userss)        # Для объеденения двух списков
print(users)

# Методы удаления из списка

users.remove("Geeks")           # Для удаление из списка по названию элемента 
print(users)

users.pop(5)        # Удаление по индексу
print(users)

# text = "Список Python — это последовательность значений любого типа: строки, числа, числа с плавающей точкой или даже смешанного типа. В этом материале речь пойдет о функциях списков, о том, как создавать их, добавлять элементы, представлять в обратном порядке и многих других."
# print(text.count("к"))

# numbers = [1,2,3,43,432,3,12,321,432,432,432,4,1,21,21,1,1,2,23,23,2,43,4,1,31,23,34,324,324,325,324,312432432]
# print(numbers.count(1))   #считает элементы внутри списка
# users.reverse()           # перевернет список
# print(users)

# users.sort()
# print(users)

users.clear()
print(users)


auto = ["Mersedes", "BMW", "TAYOTA", "Chevrale","Supra", "Nissan", "KIA", "Hyundai", "Tiko"]
name = input("Введите имя: ")
car = input("Введите название машина: ")

if car in auto:
    print(f"Уважаемый {name}, Машина есть в наличии.")
else:
    print(f"Уважаемый {name}, Машины нет в наличии.")
    
users = []

# Запросите у пользователя имя, возраст. Если пользователю есть 18 лет, должны добавить его в список users, и вывести список. Если ему нет 18 лет, вы должны вывести текст "Доступ запрещен"









