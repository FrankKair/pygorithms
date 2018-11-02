#!/usr/bin/env python3


# Fast doubling method
# https://www.nayuki.io/page/fast-fibonacci-algorithms
def fibonacci_number(n):
    def _fibonacci_number(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = _fibonacci_number(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    return _fibonacci_number(n)[0]


def sorted_digits(x):
    # Set comprehension
    return {int(x) for x in str(x)}


def pandigital_front_and_back(a, i):
    pandigital_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    if sorted_digits(a) == pandigital_set:
        fib = fibonacci_number(i)
        first_ten_digits = int(str(fib)[:9])

        if sorted_digits(first_ten_digits) == pandigital_set:
            return True

    return False


def solve():
    mod = 10**9
    a = 0
    b = 1
    index = 0
    while not pandigital_front_and_back(a, index):
        index += 1
        # Just keeps track of the last nine digits
        a, b = b, (a + b) % mod

    return index


if __name__ == '__main__':
    result = solve()
    print(result)
