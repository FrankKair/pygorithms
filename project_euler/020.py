#!/usr/bin/env python

import math


def sum_of_digits_of_factorial(x):
    factorial_string = str(math.factorial(x))
    result = 0
    for char in factorial_string:
        result += int(char)
    return result


print sum_of_digits_of_factorial(100)