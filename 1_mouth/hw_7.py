#1

# try:
#  num = int(input("Ведите первое число: "))
#  num1 = int(input("Введите второе число: "))
#  print(num/num1)

# except ZeroDivisionError:
#  print("На ноль делить нельзя!!!")

#2

# num = input("Введите имя: ")
# print(num)
# if '' in num:
#     print("Ошибка")

#3

# num = input("Введите пароль: ")
# if len(num) < 8:
#     print("Ошибка!")
# else:
#     print("Ваш пароль",num)
    
#4

# try:
#     num = int(input("Ведите первое число: "))
#     num1 = int(input("Ведите второе  число: "))
#     print(num+num1)
# except :
#     print("Ошибка!!!")
#5

# def num(*args):
#      num1 = sum(args)
#      print("Сумма аргументов равна",num1)
    
# num(1,2,3,4,5)
# num(10,20,30)
# num(5,10,15,20,25)
    
    
#6

# num2 = [3,5,6]
# num = list(map(lambda num1: num1 * 2, num2))
# print(num)
    
#7

# numu = (lambda num1:  num1 %2 == 0)
# print(numu(10))
    
#8

# num = (lambda num1: num1 ** 2)
# result = num(5)
# print(result)
    
#9

# num1 = ('Nurbolot','Aslsan','Eliza','Daiyrbek','Kudbuhon')
# sorted_list = sorted(num1, key=lambda num: len(num))
# print(sorted_list)
    
#10

# num = (lambda string, num1: num1 in string)
# num2 = num("Hello",'Erbolot')
# print(num2)
    
#11
    
# strings = lambda str1, str2: str1 + str2
# print(strings('Heloo', 'world'))

#12

# numbers = lambda numbers: list(filter(lambda x: x > 0, numbers))
# print(numbers("Hello",'world')) 

