# Задание №1

from sys import argv
name, time, zar_plat, premia = argv
print("Название скрипта ", name)
print("Время работы ", time)
print("Почасовая ставка ", zar_plat)
print("Премия ", premia)
print(f'Заработная плата сотрудника {int(time) * int(zar_plat) + int(premia)}')