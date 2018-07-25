#!/usr/bin/env python3
from math import sqrt


def right_angle_triangle_solutions_count(limit):
    l = []
    for a in range(1,limit):
        for b in range(1,limit):
            asq = a**2
            bsq = b**2
            c = int(sqrt(asq + bsq))
            csq = c**2

            if asq + bsq == csq and a + b + c == limit:
                xs = sorted([a,b,c])
                if xs not in l:
                    l.append(xs)

    return len(l)


def most_triangle_solutions():
    highest_number_of_solutions = 0
    p = 0
    for i in range(1, 1001):
        number_of_solutions = right_angle_triangle_solutions_count(i)
        if number_of_solutions > highest_number_of_solutions:
            highest_number_of_solutions = number_of_solutions
            p = i
    return p


def solve():
    return most_triangle_solutions()


if __name__ == '__main__':
    result = solve()
    print(result)
