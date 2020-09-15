def division(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        result = 'Ошибка деления на ноль!'
    return result


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
try:
    print(f'{division(float(num_1), float(num_2)): .2f}')
except ValueError:
    print('Ошибка ввода чисел!')
