#!/usr/bin/env python3
import math


def sum_of_digits_of_factorial(x):
    factorial_string = str(math.factorial(x))
    return sum([int(char) for char in factorial_string])


result = sum_of_digits_of_factorial(100)
print(result)
