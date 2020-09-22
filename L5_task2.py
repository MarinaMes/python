# алгоритм выполняется для файла, созданного в задаче 1
try:
    with open("task1.txt", "r", encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        print(f'Количество строк в файле = {len(content)}')

        f_obj.seek(0)
        num = 1
        for str in f_obj:
            list_str = str.split()
            print(f'Количество слов в строке {num} = {len(list_str)}')
            num += 1

except IOError:
    print('Ошибка работы с файлом!')
