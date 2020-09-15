def int_func(str):
    for i in list(map(ord, str)):
        if i < 65 or 91 <= i <= 96 or i > 122:
            return ''
    if str.islower():
        return (str.title())
    else:
        return ''


inp_list = input('Введите строку латинскими буквами через пробелы: ').split()
result = ''
for inp_str in inp_list:
    word = int_func(inp_str)
    result = result + (' ' + word, word)[word != '']
print(result)
