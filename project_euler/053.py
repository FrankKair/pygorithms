#!/usr/bin/env python3
import math


def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * (math.factorial(n - k)))


def solve():
    result = 0
    for n in range(1, 101):
        for k in range(1, 101):
            if n > k:
                if combination(n, k) >= 1000000:
                    result += 1

    return result


if __name__ == '__main__':
    result = solve()
    print(result)
