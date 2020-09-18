from functools import reduce

my_list = [num for num in range(100, 1001, 2)]
print(reduce(lambda arg_1, arg_2: arg_1 * arg_2, my_list))
