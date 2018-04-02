#!/usr/bin/env python3


def solve():
    number = 2**1000
    return sum([int(i) for i in str(number)])


if __name__ == '__main__':
    result = solve()
    print(result)
