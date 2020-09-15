def my_func(x, y):
    denom = x
    for i in range(1, abs(y)):
        denom *= x
    return (1 / denom)


while True:
    try:
        num_1 = float(input('Введите положительное число для возведения в степень: '))
        num_2 = int(input('Введите отрицательное целое число степени: '))

        if num_1 <= 0 or num_2 >= 0:
            print('Ошибка ввода исходных значений. Повторите ввод!')
            continue

        # вариант 1
        print(f'Вариант 1 = {(lambda x, y: pow(x, y))(num_1, num_2):.3f}')
        # вариант 2
        print(f'Вариант 2 = {my_func(num_1, num_2):.3f}')
        break
    except ValueError:
        print('Ошибка ввода исходных значений. Повторите ввод!')
