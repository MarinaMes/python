inp_text = input('Введите текст для записи в файл (для завершения пустая строка): ')
new_list = []
while bool(inp_text):
    new_list.append(inp_text + "\n")
    inp_text = input()

try:
    with open("task1.txt", "x", encoding='utf-8') as new_file:
        new_file.writelines(new_list)
except IOError:
    print('Ошибка создания файла!')
