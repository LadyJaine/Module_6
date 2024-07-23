import math
class Figure:
    sides_count = 0
    def __init__(self,color,*sides,filled = False):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = sides * 12
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        for color in [r,g,b]:
            if not (isinstance(color,int) and 0<= color <= 255):
                return False
        return True

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]

    def __is_valid_sides(self,*sides):
        # cond_1 = len(self.__sides) = len(sides)
        cond_1 = len(sides) == self.sides_count
        # if isinstance(self,Cube):
        #     cond_1 = len(sides) * 12
        # else:
        #     cond_1 = len(sides) = self.sides_count
        cond_2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond_1 and cond_2

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self,Cube):
                self.__sides = list(new_sides) * 12

            else:
                self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1


    def __init__(self,color,*sides: tuple):
        super().__init__(color, *sides)
        # self._radius = r = self.__len__() / (2 * math.pi)
        self._radius = sides[0] / (2 * math.pi)

    def get_radius(self):
        return self._radius

    def get_square(self):
        return math.pi * math.pow(self._radius, 2)

class Triangle(Figure):
    sides_count = 3

    def  get_height(self):
        s = sum(self.get_sides()) / 2
        area = math.sqrt(s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2]))
        height = 2 * area / self.get_sides()[0]
        return height


    def get_square(self):
        return self.get_sides()[0] * (self.get_height() / 2)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple,sides):
        super().__init__(color,*([sides] * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
print()
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
print()
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print()
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print()
# Проверка объёма (куба):
print(cube1.get_volume())






