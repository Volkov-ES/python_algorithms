'''9. Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).'''

n1 = int(input('Первое число n1: '))
n2 = int(input('Второе число n2: '))
n3 = int(input('Третье число n3: '))

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')
