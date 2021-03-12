'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив случайных чисел: {array}')

max = array[0]
min = array[0]

for i in array:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = array.index(min)
max_index = array.index(max)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Массив после замены элементов c индексами {min_index} и {max_index}: {array}')