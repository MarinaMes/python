def fact(n):
    for i in range(1, n + 1):
        yield i


try:
    n = int(input('Введите число для вычисления факториала:'))
    result = 1
    print(f'{n}! = 1 ', end='')
    for el in fact(n):
        result *= el
        if el != 1:
            print(f' * {el}', end='')
    print(f' = {result}')
except ValueError:
    print('Ошибка ввода!')
