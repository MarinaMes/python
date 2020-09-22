import json

try:
    new_dict = {}
    new_list = []
    sum_profit = 0
    count_firm = 0

    with open("text_7.txt", "r", encoding='utf-8') as read_f:
        for str in read_f:
            my_list = str.split()
            profit = int(my_list[2]) - int(my_list[3])
            if profit > 0:
                sum_profit += profit
                count_firm += 1
            new_dict.update({my_list[0]: profit})
        new_list = [new_dict, {'average_profit': round(sum_profit / count_firm, 2)}]
    with open("my_file.json", "w") as write_f:
        json.dump(new_list, write_f, indent=4, ensure_ascii=False)
except ValueError:
    print('Ошибка значений в файле')
except IOError:
    print('Ошибка работы с файлом!')
