# Задание №2
list = [300, 2, 48, 12, 39, 54, 5, 6, 2, 8]
new_list = [ el2 for el1, el2 in zip(list, list[1:]) if el2 > el1]
print(new_list)

# Задание №3
new_list3 = [ el for el in range(20,241) if el % 20 == 0 or el % 21 == 0 ]
print(new_list3)

# Задание №4
list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list4 = [i for i in list4 if list4.count(i) == 1]
print(new_list4)

# Задание №5
from functools import reduce
def func(el1,el2):
    return (el1*el2)
list5 = [i for i in range(99,1001) if i % 2 ==0]
print(f'Все четные числа от 100 до 1000 {[list5]}')
print(f'Произведение всех четных чисел от 100 до 1000: {reduce(func, list5)}')

# Задание №6 1 задание 1 вариант
n = int(input("Введите стартовое число "))
m = int(input("Введите конечное  число "))
list6 = [i for i in range(n,m+1)]
print(list6)

# Задание №6 1 задание 2 вариант
n1 = int(input("Введите стартовое число "))
m1 = int(input("Введите конечное  число "))
from itertools import count
for i in count(n1):
    if i > m1:
        break
    else:
        print(i)

# Задание №6 2 задание
from itertools import cycle
n2 = 0
for i in cycle("Привет"):
    if n2 > 11:
        break
    else:
        print(i)
        n2 += 1

# Задание №7

from itertools import count
from math import factorial


def generator():
    for i in count(1):
        yield factorial(i)

gen = generator()
n7 = int(input("Введите число "))
x7 = 0
for k in gen:
    if x7 < n7:
        print(k)
        x7 += 1
    else:
        break
