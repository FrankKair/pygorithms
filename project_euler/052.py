#!/usr/bin/env python3


def digits(x):
    return set([int(x) for x in str(x)])


def condition(x):
    return digits(x) == digits(2 * x) == digits(3 * x) == digits(
        4 * x) == digits(5 * x) == digits(6 * x)


def solve():
    x = 1
    while not condition(x):
        x += 1

    return x


if __name__ == '__main__':
    result = solve()
    print(result)
