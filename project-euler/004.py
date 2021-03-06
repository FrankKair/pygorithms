#!/usr/bin/env python3
def is_palindrome(number):
    return str(number)[::-1] == str(number)


def solve():
    largest_sum = 0
    for x in range(0, 1000):
        for y in range(x, 1000):
            product = x * y
            if is_palindrome(product) and product > largest_sum:
                largest_sum = product

    return largest_sum


if __name__ == '__main__':
    result = solve()
    print(result)
