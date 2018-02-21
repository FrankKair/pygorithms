#!/bin/python3
import sys


# Size -> 1, 2, 3...
# Indices -> 0, 1, 2...
# size - 1
def diagonalDifference(a):
    primary_diagonal = []
    secondary_diagonal = []

    size = len(a)
    for i, row in enumerate(range(0, size)):
        for j, column in enumerate(range(0, size)):
            if i == j:
                primary_diagonal.append(a[i][j])
            if i + j == size - 1:
                secondary_diagonal.append(a[i][j])

    return abs(sum(primary_diagonal) - sum(secondary_diagonal))


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)