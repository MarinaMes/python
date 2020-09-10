my_str = input('Пожалуйста, введите элементы списка через пробел: ')
my_list = my_str.split()

for ind, el in enumerate(my_list, 1):
    print(ind, el[:10])
