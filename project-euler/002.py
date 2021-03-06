#!/usr/bin/env python3
def sum_of_fibonacci_numbers_under(n):
    total = 0
    a = 1
    b = 2

    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    return total


def solve():
    return sum_of_fibonacci_numbers_under(4000000)


if __name__ == '__main__':
    result = solve()
    print(result)
