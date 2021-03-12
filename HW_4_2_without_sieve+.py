import timeit
import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        # for i in range(2, current_prime):
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


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
print(prime(1))

number = 1
while number < 4000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number=}\t{t_it=}\t{t_it / number =}")

# number=2      t_it=0.0005367000000000011  t_it / number =0.00026835000000000053
# number=4      t_it=0.0029206999999999983  t_it / number =0.0007301749999999996
# number=8      t_it=0.013426099999999996   t_it / number =0.0016782624999999995
# number=16     t_it=0.04451730000000001    t_it / number =0.0027823312500000006
# number=32     t_it=0.082261               t_it / number =0.00257065625
# number=64     t_it=0.22009230000000002    t_it / number =0.0034389421875000003
# number=128    t_it=0.5136050999999999     t_it / number =0.004012539843749999
# number=256    t_it=1.2283394999999997     t_it / number =0.004798201171874999
# number=512    t_it=2.8059278              t_it / number =0.005480327734375
# number=1024   t_it=7.440694399999999      t_it / number =0.007266303124999999
# number=2048   t_it=18.4085388             t_it / number =0.0089885443359375
# number=4096   t_it=52.09239900000001      t_it / number =0.012717870849609377


cProfile.run('prime(5000)')

#       4 function calls in 0.136 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.136    0.136 <string>:1(<module>)
#      1    0.136    0.136    0.136    0.136 without_sieve.py:5(prime)
#      1    0.000    0.000    0.136    0.136 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
