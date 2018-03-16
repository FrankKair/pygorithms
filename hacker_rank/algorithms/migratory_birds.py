#!/bin/python3
# https://www.hackerrank.com/challenges/migratory-birds/problem


def migratory_birds(n, ar):
    frequency_list = [0] * (n + 1)
    for index in ar:
        frequency_list[index] += 1
    return frequency_list.index(max(frequency_list))


if __name__ == '__main__':
    n = 6
    ar = [1, 4, 4, 4, 5, 3]
    result = migratory_birds(n, ar)
    print(result)
