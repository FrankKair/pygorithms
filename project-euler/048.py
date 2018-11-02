#!/usr/bin/env python3
def self_powers(limit):
    return sum((x**x for x in range(1, limit)))


def solve():
    mod = 10**10
    return self_powers(1001) % mod


if __name__ == '__main__':
    result = solve()
    print(result)
