#!/usr/bin/python3
# https://www.hackerrank.com/challenges/migratory-birds/problem
from collections import Counter


def migratory_birds(ar):
    return Counter(ar).most_common(1)[0][0]


if __name__ == '__main__':
    ar = [1, 4, 4, 4, 5, 3]
    result = migratory_birds(ar)
    print(result)
