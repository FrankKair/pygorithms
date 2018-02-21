#!/bin/python3
import sys


def staircase(n):
    max_line_size = n

    for i in range(max_line_size, 0, -1):
        number_of_spaces = i - 1

        spaces = ' ' * number_of_spaces
        symbols = '#' * (max_line_size - number_of_spaces)

        print(spaces + symbols)


if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
