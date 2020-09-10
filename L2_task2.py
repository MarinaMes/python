my_str = input('Пожалуйста, введите элементы списка через пробел: ')
my_list = my_str.split()

i = 0
while i < (len(my_list) - 1):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(my_list)
