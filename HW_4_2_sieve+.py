import timeit
import cProfile
import math

HOLE = 0
# pi_f = x // math.log(x)


def prime(num):
    # size = num ** 2 + 3
    assert num <= 5_761_455, 'Слишком большой аргумент'
    # if num > 5761455:
    #     raise Exception('Слишком большой аргумент')
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1_229: 10 ** 4,
               9_592: 10 ** 5,
               78_498: 10 ** 6,
               664_579: 10 ** 7,
               5_761_455: 10 ** 8,
               }
    for key in pi_func:
        if num <= key:
            size = pi_func[key]
            break

    array = [i for i in range(size)]

    array[1] = HOLE
    for i in range(2, size):
        if array[i] != HOLE:
            # j = i + i
            j = i ** 2
            while j < size:
                array[j] = HOLE
                j += i

    res = [i for i in array if i != HOLE]
    return res[num - 1]


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
print(prime(10))

number = 1
while number < 4000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number=}\t{t_it=}\t{t_it / number =}")

# number=2      t_it=0.003825800000000004   t_it / number =0.001912900000000002
# number=4      t_it=0.0029166999999999943  t_it / number =0.0007291749999999986
# number=8      t_it=0.02392430000000001    t_it / number =0.002990537500000001
# number=16     t_it=0.028611000000000025   t_it / number =0.0017881875000000016
# number=32     t_it=0.24387409999999998    t_it / number =0.0076210656249999995
# number=64     t_it=0.23843159999999997    t_it / number =0.0037254937499999995
# number=128    t_it=0.23993849999999994    t_it / number =0.0018745195312499996
# number=256    t_it=2.4913249              t_it / number =0.009731737890625
# number=512    t_it=2.5026221000000004     t_it / number =0.004887933789062501
# number=1024   t_it=2.556224900000001      t_it / number =0.002496313378906251
# number=2048   t_it=31.9847047             t_it / number =0.015617531591796876
# number=4096   t_it=30.311263299999993     t_it / number =0.007400210766601561


cProfile.run('prime(5000)')

#       6 function calls in 0.039 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.039    0.039 <string>:1(<module>)
#      1    0.004    0.004    0.004    0.004 sieve.py:28(<listcomp>)
#      1    0.003    0.003    0.003    0.003 sieve.py:39(<listcomp>)
#      1    0.032    0.032    0.039    0.039 sieve.py:9(prime)
#      1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(timeit.timeit('prime(1228)', number=1000, globals=globals()))
# 2.5282643000000036

print(timeit.timeit('prime(1230)', number=1000, globals=globals()))
# 32.095177899999996
