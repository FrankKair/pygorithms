# !/usr/bin/env python3


exp = 7830457
big_n = 2 ** exp
n = 28433 * big_n + 1


def digits(n):
    return [int(n) for n in str(n)]


digits = digits(n)
last_ten_slice = slice(-10, None)
result = digits[last_ten_slice]


print(result)
