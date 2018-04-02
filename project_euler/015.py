#!/usr/bin/env python3
from math import factorial


# n = steps
# k = grid size
def combination(n, k):
    return factorial(n) // (factorial(k) * (factorial(n - k)))


def count_routes(k):
    return combination(2 * k, k)


def solve():
    return count_routes(20)


if __name__ == '__main__':
    result = solve()
    print(result)
