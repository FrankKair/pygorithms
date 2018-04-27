#!/usr/bin/env python3
import os


def names():
    file = open(os.path.join(os.path.dirname(__file__), 'p022_names.txt'))
    names_list = file.read().replace('\"', '').split(',')
    return sorted(names_list)


def name_score(name):
    return sum(ord(char) - 64 for char in name)


def solve():
    names_list = names()
    total_score = 0
    for index, name in enumerate(names_list):
        score = name_score(name) * (index + 1)
        total_score += score
    return total_score


if __name__ == '__main__':
    result = solve()
    print(result)
