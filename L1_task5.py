
proceeds = float(input('Enter proceeds: '))
costs = float(input('Enter costs: '))

profit = proceeds - costs
if profit > 0:
    print('You made a profit!')
    profitab = profit / proceeds * 100
    print(f'Your profitability is {profitab:.2f} percent')

    empl = int(input('Enter number of employees'))
    profit_empl = profit / empl
    print(f'Profit per employee is {profit_empl:.2f}')
elif profit < 0:
    print('You made a loss(')
else:
    print('You hit Zero')