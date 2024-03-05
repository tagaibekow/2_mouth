#1
 
# class Fruits:
#     def __init__(self,name , color, weight):
#         self.name = name
#         self. color = color
#         self. weight = weight
#     def info(self):
#         print(f"фрукт-{self.name},цвет-{self.color},вес-{self.weight}")
    
    

# banana = Fruits('banana','yellow',200)
# apple = Fruits('apple','red','150')
# orange = Fruits('orange','green','150')

# banana.info()
# apple.info()
# orange.info()

# 2

class Car:
    def __init__(self, model , year , color):
        self.model = model
        self.year = year 
        self.color = color
        self.fuel = 0

    def drive(self,city,distens):
        self.distens = distens
        self.city=city
        print(f"машина-{self.model},едет-{self.city}")
        if self.distens > 400 and self.fuel > 40:
            print('за ваш бензин можно проехать только 400 км')

    def refuel(self, back):
        self.fuel += back
        print(f' ваш бак состовляет {self.fuel} литров')
        if back >= 40:
            print('За раз можно заправиться только до 40 литров')
        
 


car = Car("tayota camry",2018,"Black")
car.drive("osh",400)
car.refuel(40)
