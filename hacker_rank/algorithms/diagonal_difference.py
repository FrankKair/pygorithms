#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonal_difference(matrix):
    size = len(matrix)
    diff = 0
    for index in range(0, size):
        diff += matrix[index][index]
        diff -= matrix[index][size - 1 - index]

    return abs(diff)


if __name__ == "__main__":
    # 11  2  4
    # 4   5  6
    # 10  8  -12
    matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonal_difference(matrix)
    print(result)
