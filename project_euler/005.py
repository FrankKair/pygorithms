#!/usr/bin/env python3
from functools import reduce


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)


def lcm_of_sequence(seq):
    return reduce(least_common_multiple, seq)


def solve():
    return lcm_of_sequence(range(1, 20))


if __name__ == 'main':
    result = solve()
    print(result)
