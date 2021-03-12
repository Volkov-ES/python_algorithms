# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import timeit
import cProfile


def max_below_zero(size):
    # SIZE = 10
    # MIN_ITEM = -800
    # MAX_ITEM = -750
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    # print(array)

    i = 0
    index = -1

    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        # print(f'Максимальное отрицательное число {array[index]} '
        #       f'находится в ячейке {index}')
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'

'''ЗАПУСТИЛ ТО, ЧТО СДЕЛАЛИ ВЫ'''

print(timeit.timeit('max_below_zero(10)', number=1000, globals=globals()))      # 0.07429538800000002
print(timeit.timeit('max_below_zero(100)', number=1000, globals=globals()))     # 0.681215817
print(timeit.timeit('max_below_zero(1000)', number=1000, globals=globals()))    # 7.5517925660000005
print(timeit.timeit('max_below_zero(10000)', number=1000, globals=globals()))   # 77.715047466



# cProfile.run('max_below_zero(10_000)')
#         63033 function calls in 0.276 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.276    0.276 <string>:1(<module>)
#        1    0.027    0.027    0.233    0.233 hw05_tested.py:13(<listcomp>)
#        1    0.026    0.026    0.275    0.275 hw05_tested.py:9(max_below_zero)
#    10000    0.059    0.000    0.166    0.000 random.py:174(randrange)
#    10000    0.041    0.000    0.206    0.000 random.py:218(randint)
#    10000    0.066    0.000    0.106    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.276    0.276 {built-in method builtins.exec}
#    10001    0.016    0.000    0.016    0.000 {built-in method builtins.len}
#    10000    0.016    0.000    0.016    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    13027    0.024    0.000    0.024    0.000 {method 'getrandbits' of '_random.Random' objects}








##################################################################################
'''РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ ПРОГРАММЫ ПРЕПОДАВАТЕЛЕМ'''

'''
print(timeit.timeit('max_below_zero(10)', number=1000, globals=globals()))      # 0.014425200000000003
print(timeit.timeit('max_below_zero(100)', number=1000, globals=globals()))     # 0.137323
print(timeit.timeit('max_below_zero(1000)', number=1000, globals=globals()))    # 1.5733725
print(timeit.timeit('max_below_zero(10000)', number=1000, globals=globals()))   # 15.867839900000002
'''

"""
вариант запуска timeit в командной строке 
(для самостоятельного изучения любознательной частью группы)
https://docs.python.org/3/library/timeit.html
"""
# "max_below_zero(10)"
# 1000 loops, best of 5: 13.2 usec per loop
# "max_below_zero(100)"
# 1000 loops, best of 5: 128 usec per loop
# "max_below_zero(1000)"
# 1000 loops, best of 5: 1.37 msec per loop
# "max_below_zero(10000)"
# 1000 loops, best of 5: 13.6 msec per loop


# cProfile.run('max_below_zero(10_000)')
#          63153 function calls in 0.025 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#         1    0.003    0.003    0.022    0.022 hw05_tested.py:13(<listcomp>)
#         1    0.002    0.002    0.025    0.025 hw05_tested.py:9(max_below_zero)
#     10000    0.009    0.000    0.011    0.000 random.py:237(_randbelow_with_getrandbits)
#     10000    0.005    0.000    0.017    0.000 random.py:290(randrange)
#     10000    0.003    0.000    0.020    0.000 random.py:334(randint)
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#     10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13147    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#
# Process finished with exit code 0

