#!/usr/bin/env python3
def palindrome(x):
    return str(x) == str(x)[::-1]


def binary_palindrome(x):
    binary = bin(x)[2:]
    return binary == binary[::-1]


def double_base_palindrome(x):
    return palindrome(x) and binary_palindrome(x)


def double_palindrome_numbers_below(limit):
    return sum((x for x in range(1, limit) if double_base_palindrome(x)))


def solve():
    return double_palindrome_numbers_below(1000000)


if __name__ == '__main__':
    result = solve()
    print(result)
