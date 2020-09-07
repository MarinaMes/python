km_day = float(input('Enter the number of kilometers in 1 day: '))
km_result = float(input('Enter the resulting number of kilometers: '))

days = 1
while km_day < km_result:
    days += 1
    km_day = km_day + km_day * 0.1

print(f'It takes {days} days')