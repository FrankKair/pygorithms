#!/usr/bin/env python3
from collections import Counter


def socks(arr):
    pairs = 0
    c = Counter(arr)
    for value in c.values():
        if value == 1: continue
        if value % 2 == 0:
            pairs += value / 2
            continue
        value += 1
        pairs += (value / 2) - 1

    return int(pairs)


if __name__ == '__main__':
    result = socks([10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(result)
