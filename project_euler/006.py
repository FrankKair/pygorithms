#!/usr/bin/env python3


def square(number):
    return number * number


def solve():
    squared_sum = sum([square(x) for x in range(0, 101)])
    square_of_the_sum = square(sum([x for x in range(0, 101)]))
    return square_of_the_sum - squared_sum


if __name__ == 'main':
    result = solve()
    print(result)
