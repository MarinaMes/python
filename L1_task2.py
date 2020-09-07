time_sec = int(input('Enter time in seconds: '))

hours = time_sec // 3600
min = time_sec % 3600 // 60
sec = time_sec % 3600 % 60

print(f'Result: {hours:02}:{min:02}:{sec:02}')
