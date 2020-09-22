from googletrans import Translator

translator = Translator()

try:
    with open("text_4.txt", "r", encoding='utf-8') as f_obj:
        new_list = []
        for str in f_obj:
            my_list = str.split()
            ru_str = translator.translate(my_list[0], dest='ru').text
            new_list.append(str.replace(my_list[0], ru_str))

    with open("task4_new.txt", "w", encoding='utf-8') as new_file:
        new_file.writelines(new_list)
except IOError:
    print('Ошибка работы с файлом!')
