#!/usr/bin/env python3
import math


def triangle_number(x):
    return sum(range(0, x + 1))


def square_root_as_int(x):
    return int(math.sqrt(x))


def factors(number):
    factors = set()
    upper_bound = square_root_as_int(number) + 1
    for x in range(1, upper_bound):
        if number % x == 0 and number != x:
            factors.add(number / x)
            factors.add(x)
    return factors


x = 1
while len(factors(triangle_number(x))) < 500:
    x += 1

print(triangle_number(x))
