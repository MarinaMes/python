def my_func(*arg):
    my_list = list(arg)
    my_list.remove(min(my_list))
    return sum(my_list)


inp_list = input('Введите 3 числа через пробел: ').split()
try:
    nums = list(map(float, inp_list))
    print(my_func(nums[0], nums[1], nums[2]))
except (ValueError, IndexError):
    print("Ошибка ввода строки чисел!")
