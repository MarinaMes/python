my_list = [7, 5, 3, 3, 2]

while True:
    num = input('Введите натуральное число: ')
    if num.isdigit():
        num = int(num)
        pos = 0
        if num <= my_list[len(my_list) - 1]:
            my_list.append(float(num))
        else:
            for ind in range(len(my_list)):
                if my_list[ind] < num:
                    pos = ind
                    break
            my_list.insert(pos, float(num))
        break
    else:
        print('Нужно ввести натуральное число!')

print(my_list)
