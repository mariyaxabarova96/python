# Задание №1
from time import sleep

class TrafficLight:
     __color = ['Красный', 'Желтый', 'Зеленый']

     def running(self):
         i = 0
         while i != 3:
             print(TrafficLight.__color[i])
             if i == 0:
                 sleep(7)
             elif i == 1:
                 sleep(2)
             elif i == 2:
                 sleep(1)
             i += 1

t = TrafficLight()
t.running()

# Задание №2

class Road:
    def __init__(self, length, width, massa_na_1sm, height):
        self._length = length
        self._width = width
        self._massa_na_1sm = massa_na_1sm
        self._height = height

    def result(self):
        result_mass = self._width * self._length * self._massa_na_1sm * self._height / 1000
        print(f'Необходимая масса асфальта {result_mass} т')


m = Road(20, 10000, 25, 10)

m.result()

# Задание №3

class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": int(salary), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        print(f'Имя сотрудника {self.name}')
        print(f'Фамилия сотрудника {self.surname}')
        print(f'Должность сотрудника {self.position}')

    def get_total_income(self):
        print(f'Заработная плата сотрудника {self._income["salary"] + self._income["bonus"]}')

n =Position('Петя','Петров', 'инженер', 20000, 5000)
print(n.name)
print(n.surname)
print(n.position)
print(n._income)
n.get_full_name()
n.get_total_income()

# Задание №4
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        return self.is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_right(self):
        print('Машина повернула направо')

    def turn_left(self):
        print('Машина повернула налево')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена на {self.speed - 60} км/ч")
        else:
            print(f'Текущая скорость автомобиля {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена на {self.speed - 40} км/ч")
        else:
            print(f'Текущая скорость автомобиля {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


b = TownCar(90, "white", "lada", False)
b.show_speed()
print(b.name)
print(b.speed)
print(b.color)
b.go()
b.stop()
b.turn_left()
b.turn_right()
b.show_speed()
print(b.police())

s = Car(30, 'red', "Suzuki", False)
print(s.name)
print(s.speed)
print(s.color)
s.go()
s.stop()
s.turn_left()
s.turn_right()
s.show_speed()
print(s.police())

# Задание №5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Сегодня рисуем {self.title} ')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Сегодня рисуем {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Сегодня рисуем {self.title}')

q = Pen('ручкой')
q.draw()

w = Pencil('карандашом')
w.draw()

e = Handle('маркером')
e.draw()