my_base = []
keys = ['название', 'цена', 'количество', 'ед']
count = 1

menu = ''
while menu != '4':
    menu = input('Выберите действие: 1 - добавить товар, 2 - посмотреть товары, 3 - получить аналитику, 4 - выход ')
    if menu == '1':
        new_dict = {}
        for key in keys:
            new_char = input(f'Введите характеристику <{key}> товара ')
            if new_char.isdigit():
                new_char = int(new_char)
            new_dict.update({key: new_char})
        new_list = [count, new_dict]
        my_base.append(tuple(new_list))
        count += 1
    elif menu == '2':
        for el in my_base:
            print(f'{el[0]} - {el[1]}')
    elif menu == '3':
        dict_stat = {'название': [], 'цена': [], 'количество': [], 'ед': []}
        for el in my_base:
            for key in dict_stat.keys():
                pos = el[1].get(key)
                if pos in dict_stat[key]:
                    continue
                else:
                    dict_stat[key].append(pos)
        print(dict_stat)
