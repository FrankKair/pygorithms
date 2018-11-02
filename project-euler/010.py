#!/usr/bin/env python3
from itertools import takewhile


def primes():
    D = {}
    q = 2

    while True:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D:
                x += p
            D[x] = p
        else:
            D[q * q] = q
            yield q
        q += 1


def solve():
    return sum(takewhile(lambda x: x < 2000000, primes()))


if __name__ == '__main__':
    result = solve()
    print(result)
