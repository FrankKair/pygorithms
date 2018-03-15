#!/bin/python3
import sys


def migratoryBirds(n, ar):
    frequency_list = [0] * (n + 1)
    for index in ar:
        frequency_list[index] += 1
    return frequency_list.index(max(frequency_list))


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = migratoryBirds(n, ar)
    print(result)
