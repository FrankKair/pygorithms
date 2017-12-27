#!/usr/bin/env python
import math


def square_root_int(x):
    return int(math.sqrt(x))


def is_prime(number):
    if number == 1:
        return False
    upper_bound = square_root_int(number) + 1
    for x in range(2, upper_bound):
        if x == number:
            next
        if number % x == 0:
            return False
    return True


def factors_of(number):
    factors = []
    upper_bound = square_root_int(number) + 1
    for x in range(2, upper_bound):
        if number % x == 0:
            factors.append(x)
            factors.append(number / x)
    return factors


factors = factors_of(600851475143)
maximum_value = max([x for x in factors if is_prime(x)])
print(maximum_value)
