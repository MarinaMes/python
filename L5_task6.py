def numbers(text1):
    result = ''
    for i in text1:
        if i.isdigit():
            result = result + i
    return result


try:
    new_dict = {}
    with open("text_6.txt", "r", encoding='utf-8') as f_obj:
        for str in f_obj:
            my_list = str.split()
            hours = [numbers(el) for el in my_list[1:] if bool(numbers(el))]
            new_dict.update({my_list[0]: sum(map(int, hours))})
    print(new_dict)
except IOError:
    print('Ошибка работы с файлом!')
