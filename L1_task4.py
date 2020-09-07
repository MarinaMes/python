num = int(input('Enter positive integer: '))

max = 0
while num != 0:
    num_test = num % 10
    if num_test > max:
        max = num_test
    num = num // 10

print(f'Maximum number = {max}')
