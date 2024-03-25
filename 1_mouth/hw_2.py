# 1

# number = input("Введите слова: ")
# print(number[::-1])

#2

# string = input("Введите слова: ")
# print(string[0])
# print(string[-1])
# print(string[1:-1])

#3

# order = int(input("Введите сумму заказа: "))
# if order < 1000:
#     deliver = 200 
# elif 1000 <= order <= 5000:
#     deliver = 100 
# else:
#     deliver = "бесплатная"

# print(f"{deliver} доставка")

#4

# grade = int(input("Оценка студента: "))
# if grade >= 60:
#     print("Вы прошли")
# else:
#     print("Не прошли:")
    
 #5
 
# wer = int(input("Введите целое число: "))
# if wer % 2 == 0:
#     print("четное")
# else:
#     print("не четное")
  
#7

# name1 = "Aidana"
# name2 = "Adilet"
# print(name1[0],name2[0],name1[1],name2[1],name1[2],name2[2],name1[3],name2[3],name1[4],name2[4],name1[5],name1[5])

#Доп 

# grade = int(input('Введите оценку: '))
# if  grade < 90:
#      print("Отлично")
# elif 80 <= grade < 90:
#     print("Хорошо")
# elif 70 <= grade < 80:
#     print("Удовлетворительно")
# elif 60 <= grade < 70:
#     print("Неудовлетворительно")
# else:
#     print("Студент должен пересдать экзамен")

num = [1,2,3,4,5]
numu=num.pop(0,2)
print(numu)