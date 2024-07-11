class Vehicle:
    __color_variants = ['red', 'blue', 'yellow', 'black', 'grey']
    def __init__(self,owner:str,__model:str,__engine_power:int,__color:str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return(f"Модель: {self.__model}")

    def get_horsepower(self):
        return(f"Мощность двигателя:{self.__engine_power}")

    def get_color(self):
        return(f"Цвет: {self.__color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец:{self.owner}")


    def set_color(self,new_color:str):
        # self.new_color = new_color
        if new_color.lower in self.__color_variants:
            self.__color == new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")



class Sedan(Vehicle):
    def __init__(self,owner,__model,__engine_power,__color,__PASSENGERS_LIMIT = 5):
        super().__init__(owner,__model,__engine_power,__color)
        self.__PASSENGERS_LIMIT = __PASSENGERS_LIMIT

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()
print()
# Изначальные свойства
vehicle1.print_info()
print()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
print()
vehicle1.set_color('BLACK')
print()
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()