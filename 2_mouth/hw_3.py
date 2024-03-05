class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu
    @property
    def memory(self):
        return self.__memory
        
    def __make_computations(self):
        print(f"""Результат сложение: {self.cpu + self.memory}
Результат вычитание: {self.cpu - self.memory}
Результат умножение: {self.cpu * self.memory}
Результат деление: {self.cpu / self.memory}""")    
    @property
    def make_computations(self):
        return self.__make_computations
    

laptop = Computer(34,516)
laptop.make_computations()

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        Computer.__init__(self, cpu, memory)
        self.__memory_card = memory_card
        
    @property
    def memory_card(self):
        return self.__memory_card
    def info(self):
        print(f"процессор - {self.cpu}, память - {self.memory}, карта памяти - {self.memory_card}")

comp = Laptop("core-i5", 256, 128)
comp.info()
        
        