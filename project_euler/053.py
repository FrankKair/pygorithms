#!/usr/bin/env python3
from math import factorial


def combination(n, k):
    return factorial(n) // (factorial(k) * (factorial(n - k)))


def solve():
    return sum(1 for x in range(1, 101) for y in range(1, 101)
               if x > y and combination(x, y) >= 1000000)


if __name__ == '__main__':
    result = solve()
    print(result)
