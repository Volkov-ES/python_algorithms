'''1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'''


start_num = 2
end_num = 99
start_div = 2
end_div = 9

result = {}
for n in range(start_div, end_div + 1):
    result[n] = []
    for f in range(start_num, end_num + 1):
        if f % n == 0:
            result[n].append(f)
    print(f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.')