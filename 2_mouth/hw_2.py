#1

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Mеня зовут {self.fullname}. Мне {self.age} лет.")
        if self.is_married:
            print("Я женат.")
        else:
            print("Я не женат.")

person1 = Person("Байбалаев Аслан", 22, False)
person1.introduce_myself()

#2

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

teacher1 = Teacher("Байбалаев Аслан", 22, False, 10)
print(teacher1.fullname)  
print(teacher1.age)      
print(teacher1.is_married) 
print(teacher1.experience) 

#Доп дз

class Teacher(Person):
    salary = 0  

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        self.salary = Teacher.salary + 3000 * self.experience

    def introduce_myself(self):
        super().introduce_myself()
        print(f"У меня {self.experience} лет опыта преподавание.")
        print(f"Мой зарплата состовляет {self.salary} сомов.")

teacher1 = Teacher("Байбалаев Аслан", 22, False, 10)
teacher1.calculate_salary()
teacher1.introduce_myself()

