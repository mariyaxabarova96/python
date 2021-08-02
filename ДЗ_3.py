# Задание №1
def first_function(m, n):
    if n != 0:
        k =  m / n
        return k
    else:
        print("Error")

print(first_function(int(input("Введите первое число ")), int(input("Введите второе число "))))

# Задание №2
def second_function (name, surname, b_year, city, email, phone):
    return (','.join([name, surname, b_year, city, email, phone]))

print(second_function(input("Введите имя "), input("Введите фамилию "), input("Введите год рождения "), input("Введите город рождения "), input("Введите email "), input("Введите номер телефона ")))

# Задание №3
def third_function (x,y,z):
    list = [x, y, z]
    list.remove(min(list))
    return sum(list)

print(third_function(int(input("Введите первое число ")), int(input("Введите второе число ")), int(input("Введите третье число "))))

# Задание №4 (первый способ)
def fourth_func (x,y):
    m = x ** y
    return m
print(fourth_func(int(input("Введите первое число ")), int(input("Введите второе число "))))

# Задание №4 (второй способ)
def fourth_func_2 (x,y):
    min = abs(y)
    res = x
    new_res = x
    for i in range(min-1):
        res = res * new_res
        i += 1
        return 1 / res

print(fourth_func_2(int(input("Введите первое число ")), int(input("Введите второе число "))))

# Задание №5
def fifth_func ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или нажмите + ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == '+':
                ex = True
                break
            else:
                res = res + int(number[el])
            sum_res = sum_res + res
            print(f'Промежуточное значение суммы {sum_res}')
    print(f'Финальное значение суммы {sum_res}')

fifth_func()

# Задание №6

def sixth_func (a):
    a.split(' ')
    return a.title()


print(sixth_func(input("Введите строку ")))


