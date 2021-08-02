#Домашнее задание 2
#Задание №1
my_list = ['a', 'abc', 1, 16.6, True]
for i in my_list:
    print(i, type(i))

#Задание №2
obmen_list = []
n = int(input("Введите количество элементов списка "))
i = 0
el = 0
for i in range(n):
    obmen_list.append(input("Введите элементы списка "))
    i += 1
for elem in range(int(len(obmen_list)/2)):
        obmen_list[el], obmen_list[el + 1] = obmen_list [el + 1], obmen_list[el]
        el += 2
print(obmen_list)

#Задание №3
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите номер месяца "))
if month ==1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

# Задание №4
stroka = str(input("Введите строку "))
n = 1
if len(stroka)<= 10:
    a = list(stroka.split())
    b = len(a)
    for i in range(b):
        print(f'{n}. {a[n-1]}')
        n = n + 1
else:
    a = list(stroka.split())
    b = len(a)
    for i in range(b):
        print(f'{n}. {a[n - 1] [0:10]}')
        n = n+1


#Задание №5
my_list  = [7, 3, 2, 1, 8]
for i in my_list:
    my_list.append(int(input("Введите число ")))
    my_list.sort()
    my_list.reverse()
    print(my_list)
    break

#Задание №6
my_list = []
i = 1
while True:
    my_list.append(
        (input('Введите номер товара: '), dict({
            'название': str(input('Введите название: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единцы измерения: ')),
        }))
    )

    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
        break

    i += 1

print(f'список товаров:{my_list}')

output_dict = dict({})
for product in my_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'собрана аналитика: {output_dict}')