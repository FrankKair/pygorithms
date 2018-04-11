#!/usr/bin/env python3


def solve():
    l = [1]
    for grid_size in range(3, 1003, 2):
        start = l[len(l) - 1]
        interval = grid_size - 1
        diagonal_numbers = [
            start + interval,
            start + (2 * interval),
            start + (3 * interval),
            start + (4 * interval)
        ]
        l.extend(diagonal_numbers)
    return sum(l)


if __name__ == '__main__':
    result = solve()
    print(result)

