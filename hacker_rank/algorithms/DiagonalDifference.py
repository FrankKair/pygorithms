#!/usr/bin/env python3
import sys


# Size -> 1, 2, 3...
# Indices -> 0, 1, 2...
# size - 1
def diagonalDifference(a):
    size = len(a)
    diff = 0
    for index in range(0, size):
        diff += a[index][index]
        diff -= a[index][size - 1 - index]

    return abs(diff)


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)
