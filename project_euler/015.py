#!/usr/bin/env python3
import math


# n = steps
# k = grid size
def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * (math.factorial(n - k)))


def count_routes(k):
    return combination(2 * k, k)


def solve():
    return count_routes(20)


if __name__ == 'main':
    result = solve()
    print(result)
