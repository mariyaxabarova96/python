#Задание №1

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4d}", end="")
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
new_m = Matrix([[-1, -2, -3, -5], [-1, -2, -3, -5], [-1, -2, -3, -5]])
print(m.__add__(new_m))

# Задание №2
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def summa(self):
        print (f'Для пошива необходимо {self.param/6.5 + 0.5 + 2*self.param + 0.3}')

    @abstractmethod
    def name(self):
        print(f'Это одежда сшита на заказ по вашим меркам')


class Palto (Clothes):
    def summa(self):
        print(f'Для изготовления пальто необходимо {self.param / 6.5 + 0.5 } м ткани')

    def name(self):
        print(f'Это одежда сшита на заказ по вашим меркам')

class Kost(Clothes):
    def summa(self):
        print(f'Для изготовления костюма необходимо {2 * self.param + 0.3 } м ткани')

    def name(self):
        print(f'Это одежда сшита на заказ по вашим меркам')

a = Palto(130)
a.summa()
b= Kost(50)
b.summa()
b.name()
print()

# Задание №3

class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        print(f'Сумма ячеек клетки {self.number + other.number}')

    def __sub__(self, other):
        sub = self.number - other.number
        if sub > 0:
            print(f'Разность между количеством ячеек равна {sub}')
        else:
            print('Клетки больше не существует')

    def __truediv__(self, other):
        return self.number // other.number

    def __mul__(self, other):
        return self.number * other.number

    def make_order(self, row):
        result = ''
        for i in range(int(self.number / row)):
            result += '*' * row + '\n'
        result += '*' * (self.number % row) + '\n'
        return result


m = Cell(30)
n = Cell(2)
print(m + n)
print(m - n)
print(m / n)
print(m * n)
print(m.make_order(7))

