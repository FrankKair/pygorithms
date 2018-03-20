#!/usr/bin/env python3


def solve():
    return sum([x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0])


if __name__ == '__main__':
    result = solve()
    print(result)