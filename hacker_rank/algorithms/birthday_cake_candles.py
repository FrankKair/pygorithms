#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
from collections import Counter


def count_candles(ar):
    c = Counter(ar)
    highest_key = sorted(c)[-1]
    return c[highest_key]


if __name__ == '__main__':
    ar = [3, 2, 1, 3]
    result = count_candles(ar)
    print(result)
