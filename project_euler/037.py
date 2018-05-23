#!/usr/bin/env python3
from math import sqrt


def square_root_int(x):
    return int(sqrt(x))


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


def truncatable(number):
    size = len(str(number))
    for i in range(0, size):
        n = str(number)
        
        # Truncate left
        left = int(n[i : size])

        # Truncate right
        right = int(n[:size - i])

        if not (is_prime(left) and is_prime(right)):
            return False

    return True


def sum_n_truncatable_primes(n):
    truncatable_primes = []
    number = 11
    while not len(truncatable_primes) == n:
        if truncatable(number):
            truncatable_primes.append(number)
        number += 2
    return sum(truncatable_primes)


def solve():
    return sum_n_truncatable_primes(11)


if __name__ == '__main__':
    result = solve()
    print(result)
