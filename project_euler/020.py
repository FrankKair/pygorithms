#!/usr/bin/env python3
from math import factorial


def sum_factorial_digits(x):
    factorial_string = str(factorial(x))
    return sum(int(char) for char in factorial_string)


def solve():
    return sum_factorial_digits(100)


if __name__ == '__main__':
    result = solve()
    print(result)
