try:
    my_str = input('Введите числа, разделенные пробелом ')
    with open("task5.txt", "w+", encoding='utf-8') as new_file:
        new_file.write(my_str)
        new_file.seek(0)
        print(sum(map(int, new_file.read().split())))
except IOError:
    print('Ошибка работы с файлом!')
except ValueError:
    print('Ошибка ввода строки чисел!')
