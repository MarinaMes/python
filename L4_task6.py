from sys import argv
from itertools import count, cycle, islice

try:
    script_name, num = argv
    my_list = [el for el in islice(count(int(num)), 10)]
    print(my_list)

    new_gen = cycle(my_list)
    ind = 0
    new_list = []
    while ind < 25:
        new_list.append(next(new_gen))
        ind += 1
    print(new_list)
except ValueError:
    print('Input error!')
