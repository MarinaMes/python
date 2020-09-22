try:
    with open("text_3.txt", "r", encoding='utf-8') as f_obj:
        sum = 0
        num = 0
        print(f'Список сотрудников с заработной платой менее 20000: ')
        for str in f_obj:
            list_str = str.split()
            if float(list_str[1]) < 20000:
                print(list_str[0])
            sum += float(list_str[1])
            num += 1
        print(f'Средняя заработная плата составляет {round(sum / num, 2)}')
except IOError:
    print('Ошибка работы с файлом!')
