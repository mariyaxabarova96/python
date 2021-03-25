# Домашнее задание 2
# Задание 1
# my_list = ['a', 'abc', 1, 16.6, True]
# for i in my_list:
#     print(i, type(i))
    # Задание 2
    # obmen_list = []
    # n = int(input("Введите количество элементов списка "))
    # for i in range(n):
    #     obmen_list.append(input())
    # if len(obmen_list) % 2 == 0:
    #     i = 0
    #     while i < len(obmen_list):
    #         el = obmen_list[i]
    #         obmen_list[i] = obmen_list[i + 1]
    #         obmen_list[i + 1] = el
    #         i += 2
    # else:
    #     i = 0
    #     while i < len(obmen_list) - 1:
    #         el = obmen_list[i]
    #         obmen_list[i] = obmen_list[i + 1]
    #         obmen_list[i + 1] = el
    #         i += 2
    # print(obmen_list)

# Задание 3
# seasons_list = ['winter', 'spring', 'summer', 'autumn']
# seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
# month = int(input("Введите месяц по номеру "))
# if month ==1 or month == 12 or month == 2:
#         print(seasons_dict.get(1))
#         print(seasons_list[0])
# elif month == 3 or month == 4 or month ==5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
#
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#         print("Такого месяца не существует")

# # Задание 4
# stroka = str(input("Введите строку "))
# n = 1
# if len(stroka)<= 10:
#     a = list(stroka.split())
#     b = len(a)
#     for i in range(b):
#         print(f'{n}. {a[n-1]}')
#         n = n + 1
# # else:
# #     a = list(stroka.split())
# #     b = len(a)
# #     for i in range(b):
# #         # a = list(stroka.split())
# #         print(f'{n}. {a[n - 1]}')
# #         n = n + 1

inventory_tuple_list = []
i = 1
while True:
    inventory_tuple_list.append(
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

print(f'список товаров:{inventory_tuple_list}')

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'собрана аналитика: {output_dict}')


