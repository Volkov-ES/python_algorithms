# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import timeit
import cProfile


def max_below_zero_while(array):
    i = 0
    index = -1

    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


def max_below_zero_for(array):
    index = -1

    for i in range(len(array)):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i

    if index != -1:
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


def max_below_zero_enumerate(array):
    max_below = index = None

    for i, item in enumerate(array):
        if item < 0 and max_below is None:
            max_below = item
            index = i
        elif 0 > item > max_below:
            max_below = item
            index = i

    if max_below is not None:
        return f'Максимальное отрицательное число {max_below} ' \
               f'находится в ячейке {index}'


with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f'size,while,for,enumerate\n')
    for size in range(100, 10_001, 100):
        data = [random.randint(size * -10, size * 10) for _ in range(size)]
        whi_ = timeit.timeit('max_below_zero_while(data)', number=1000, globals=globals())
        for_ = timeit.timeit('max_below_zero_for(data)', number=1000, globals=globals())
        enu_ = timeit.timeit('max_below_zero_enumerate(data)', number=1000, globals=globals())
        f.write(f'{size},{whi_},{for_},{enu_}\n')

