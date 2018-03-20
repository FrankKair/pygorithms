#!/usr/bin/env python3
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


def solve():
    factors = factors_of(600851475143)
    return max([x for x in factors if is_prime(x)])


if __name__ == '__main__':
    result = solve()
    print(result)