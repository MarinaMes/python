from sys import argv

try:
    script_name, hours, rate, bonus = argv
    salary = float(hours) * float(rate) + float(bonus)
    print(salary)
except ValueError:
    print('Input error!')
