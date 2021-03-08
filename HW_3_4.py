'''4. Определить, какое число в массиве встречается чаще всего.'''

'''ВОПРОС: Как сделать программу для случаев когда в массиве встречается чаще всего более одного числа?'''



import random

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE) for _ in range(SIZE)]
print(f'Массив случайных чисел: {array}')

number = array[0]
max_frequency = 1
for i in range(SIZE - 1):
    frequency = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            frequency += 1
    if frequency > max_frequency:
        max_frequency = frequency
        number = array[i]
 
if max_frequency > 1:
    print(max_frequency, 'раз(а) встречается число', number)
else:
    print('Все элементы уникальны.')

