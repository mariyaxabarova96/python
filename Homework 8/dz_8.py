# Задание №1

class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def data_new(cls, data):
        my_date = [i for i in data.split() if i != '-']
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):

        if day > 0 and day <= 31:
            print("Day is ok")
            if month > 0 and month <= 12:
                print("Month is ok")
                if year > 0 and year<=2022:
                    print("Year is ok")
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")



today = Data('16 - 07 - 1996')
print(Data.data_new('16 - 07 - 1996'))
print(today.data_new('16 - 22 - 1915'))
Data.validation(16, 12, -1952)

# Задание №2

class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def delenie(x,y):
        try:
            return x / y
        except:
            return (f'На ноль делить нельзя')
print()
print(V.delenie(5, 0))
print(V.delenie(10, 2))

# Задание №3

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())

# Задание №4-6

class Sklad:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
        self.my_store.append(self.my_unit)
    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Наименование': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_store.append(unique)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input()
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'

        else:
            return Sklad.reception(self)


class Printer(Sklad):
    def to_print(self):
        return ('Это принтер')


class Scanner(Sklad):
    def to_scan(self):
        return ('Это сканер')


class Copier(Sklad):
    def to_copier(self):
        return ('Это ксерокс')


unit_1 = Printer('hp', 2000, 5, 10)
print(unit_1.reception())
print(unit_1.to_print())

# Задание №7

class Dif_Numb:
    def __init__(self, m, n):
        self.m = m
        self.n = n


    def __add__(self, other):
        print(f'Сумма комплексных чисел равна')
        return f'z = {self.m + other.m} + {self.n + other.n} * i'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'z = {self.m * other.m - (self.n * other.n)} + {self.m * other.m} * i'

    def __str__(self):
        return f'z = {self.m} + {self.n} * i'


z_1 = Dif_Numb(1, -2)
z_2 = Dif_Numb(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)