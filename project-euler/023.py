#!/usr/bin/env python3
import math
from itertools import combinations_with_replacement


def divisors(number):
    factors = set()
    upper_bound = int(math.sqrt(number)) + 1
    for x in range(2, upper_bound):
        if number % x == 0:
            factors.add(x)
            factors.add(number / x)
    return factors


def is_abundant(x):
    return sum(divisors(x)) > x


def solve():
    """
    Sum of all positive integers that cannot be
    written as the sum of two abundant numbers.

    It can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers.
    """
    limit = 28124
    abundant_numbers = [x for x in range(1, limit) if is_abundant(x)]
    combinations = combinations_with_replacement(abundant_numbers, 2)
    possible_sums = set(x[0] + x[1] for x in combinations)
    return sum(x for x in range(1, limit) if x not in possible_sums)


if __name__ == '__main__':
    result = solve()
    print(result)
