# Задание №1

my_f6_1 = open('dz6.1.txt', 'w')
while True:
    line = input('Введите текст \n')
    my_f6_1.writelines(line)
    if not line:
        print("Данных больше нет ")
        break
my_f6_1.close()

# Задание №2

my_f6_2 = open('dz6.2.txt', 'r')
count = 0
for i in my_f6_2:
    count = count+1

print (f'Количество строк -  {count}')
my_f6_2.close()

with open('dz6.2.txt') as f:
    n = 0
    for line in f:
        words = line.split()
        n = len(words)
        print(f'Количество слов в строке {n}')

# Задание №3

with open('dz6.3.txt', 'r') as my_f6_3:
    payment = []
    surname = []
    my_list3 = my_f6_3.read().split('\n')
    for i in my_list3:
        i = i.split()
        if int(i[1]) < 20000:
            surname.append(i[0])
            payment.append(i[1])
print(f'Оклад меньше 20.000 {surname}, средний оклад {sum(map(int, payment)) / len(payment)}')

# Задание №4

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('dz6.4.txt', 'r') as my_f6_4:
    for i in my_f6_4:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])


with open('dz6.4.1.txt', 'w') as my_f6_4_1:
    my_f6_4_1.writelines(new_file)

# Задание №5

def summa():
    with open('dz6.5.txt', 'w+') as my_f6_5:
        line = input('Введите числа через пробел \n')
        my_f6_5.writelines(line)
        numb = line.split()
        print(sum(map(int, numb)))
summa()

# Задание №6
subjects = {}
with open('dz6.6.txt', 'r') as my_f6_6:
    lines = my_f6_6.readlines()
    for line in lines:
        new_line = line.replace('(', ' ').replace(')', ' ').split()
        subjects[new_line[0][:-1]] = sum(int(i) for i in new_line if i.isdigit())
print(subjects)
print(type(subjects))

# Задание №7
import json
pribil = {}
sr_pribil = {}
m = 0
d = 0
i = 0
list = []
srednee = 0
with open('dz6.7.txt', 'r') as my_f6_7:
    lines = my_f6_7.readlines()
    for line in lines:
        name, a, b, c = line.split()
        raznica = int(b) - int(c)
        pribil[name] = raznica
        if int(raznica) >= 0:
            m = m + raznica
            d = d + 1
    if d != 0:
        srednee = m / d
        print(f'Средняя выручка {srednee}')
    else:
        print('Прибыль отсутствует')
    sr_pribil['average'] = srednee
    list = [pribil, sr_pribil]
    print(list)

with open('dz_7.json', 'w') as write_js:
    json.dump(list, write_js)

    js_str = json.dumps(list)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')









