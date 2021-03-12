import timeit
import cProfile
import math

HOLE = False


def prime(num):
    multiplier = 1.3
    size = int(num * math.log(num) * multiplier) if num > 10 else 30

    array = [True for _ in range(size)]
    array[:2] = [HOLE, HOLE]
    count = 0

    for i in range(2, size):
        if array[i]:

            count += 1
            if count == num:
                return i

            for j in range(i ** 2, size, i):
                array[j] = HOLE


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
"""Поиск большого простого числа на 32х Python выдал ошибку MemoryError
Но на 64х версии интерпретатора код успешно завершился
print(timeit.timeit('prime(10_000_000)', globals=globals(), number=1))
# Ответ: 179424673 Время: 54.154248359339334
"""

number = 1
while number < 16000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number=}\t{t_it=}\t{t_it / number =}")

# number=2      t_it=0.004134799999999994   t_it / number =0.002067399999999997
# number=4      t_it=0.0060433000000000014  t_it / number =0.0015108250000000004
# number=8      t_it=0.004758999999999999   t_it / number =0.0005948749999999999
# number=16     t_it=0.012488699999999991   t_it / number =0.0007805437499999995
# number=32     t_it=0.023932199999999987   t_it / number =0.0007478812499999996
# number=64     t_it=0.055452               t_it / number =0.0008664375
# number=128    t_it=0.14081200000000002    t_it / number =0.0011000937500000002
# number=256    t_it=0.3485395              t_it / number =0.001361482421875
# number=512    t_it=0.7077077              t_it / number =0.0013822416015625
# number=1024   t_it=1.5482496000000001     t_it / number =0.0015119625000000001
# number=2048   t_it=3.5068982999999996     t_it / number =0.0017123526855468748
# number=4096   t_it=7.4202434              t_it / number =0.001811582861328125
# number=8192   t_it=16.532505399999998     t_it / number =0.0020181281005859373
# number=16384  t_it=40.1398753             t_it / number =0.0024499435607910156


cProfile.run('prime(5000)')

#       6 function calls in 0.013 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#      1    0.002    0.002    0.002    0.002 sieve_plus.py:12(<listcomp>)
#      1    0.011    0.011    0.013    0.013 sieve_plus.py:8(prime)
#      1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

