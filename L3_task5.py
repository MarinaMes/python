def my_func(result):
    my_list = input('Введите последовательность целых чисел через пробелы (для выхода %): ').split()
    try:
        if '%' in my_list:
            pos = my_list.index('%')
            result += sum(list(map(int, my_list[:pos])))
        else:
            result += sum(list(map(int, my_list)))
            print(f'Промежуточный итог = {result}')
            result = my_func(result)
        return (result)
    except ValueError:
        pass


print(f'Итоговая сумма = {my_func(0)}')
