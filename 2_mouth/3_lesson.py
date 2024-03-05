# Инкапcуляция

# class SmartPhone:
#     def __init__(self, sim_cards, battery):
#         self.__sim_cards = sim_cards
#         self.battery = battery

#     @property
#     def sim_cards(self):
#         return self.__sim_cards
    
#     @sim_cards.setter
#     def sim_cards(self, sim):
#         self.sim_cards == sim

#     def __info(self):
#         print(f'Ваши сим карты {self.sim_cards}, Ваш объем батареи {self.battery}')

#     @property
#     def info(self):
#         return self.__info
    
# poco = SmartPhone(['Megacom', 'O!'], 300)
# poco.info()


# Множественное наследование

# class Car:
#     def __init__(self, model, year):
#         self.model = model 
#         self.year = year

#     def info(self):
#         print(f'Бренд машины - {self.model}, год выпуска - {self.year}')

# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self, model, year)
#         self.battery = battery

#     def drive(self):
#         print(f'{self.model}, едет на электричестве')

# class FuelCar(Car):
#     def __init__(self, model, year, fuel_bak):
#         Car.__init__(self, model, year)
#         self.fuel_bak = fuel_bak

#     def drive(self):
#         print(f'{self.model}, едет на Топливо!')


# class HybridCar(ElectricCar, FuelCar):
#     def __init__(self, model, year, fuel_bak, battery):
#         ElectricCar.__init__(self, model, year, battery)
#         FuelCar.__init__(self, model,year,fuel_bak)

#     def drive(self):
#         print(f"{self.model}, едет на Топливо! и на электричестве ")   

# tesla = ElectricCar('Tesla Model X', 2020, 150000)
# tesla.info()
# tesla.drive()

# audi = FuelCar('R-8', 2018, 15)
# audi.info()
# audi.drive()

# toyta = HybridCar('Avalon', 2023, 1000000, 10)
# toyta.info()
# toyta.drive()


class laptop():
    def __init__(self, model, year, core, color):
        self.model = model
        self.year = year 
        self.core = core
        self.color = color
        
    def lenovo(self):
        print(f"Модель {self.model},год выпуска-{self.year},паколения-{self.core},цвет-{self.color}")
        
    def info(self):
        print(lenovo)    
    
class Mac(laptop):
    def __init__(self, model, year, core, color):
        laptop.__init__(model, year, color)
        self.core = core
        
class Acer(laptop):
    def __init__(self, model, year, core, color):
        laptop.__init__(self, year, model, color)
        self.core = core
        
class AcMac(Mac, Acer):
    def __init__(self, model, year, core, color):
        Mac,Acer.__init__(self, model, year, color)
        self.core = core
        
lenovo = laptop('lenovo', 2020, 'core i5','черный')
lenovo.info()


Macbook = ('Macbook pro', 2021, 'серый')
Macbook.info()
Macbook.core()

acer = Acer('Acer', 'core i3', 'серый')
acer.info()
acer.year()

acmac = AcMac('AcMac pro max', 2024, 'core i15')
acmac.info()
acmac.color()
