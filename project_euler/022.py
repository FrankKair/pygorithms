#!/usr/bin/env python3
import os


def name_score(name):
    return sum([ord(char) - 64 for char in name])


def remove_quotes(string):
    return string.strip('\"')


def names():
    file = open(os.path.join(os.path.dirname(__file__), 'p022_names.txt'))
    return sorted(file.read().split(','))


def solve():
    names_list = names()

    total_score = 0
    for index, name in enumerate(names_list):
        name = remove_quotes(name)
        score = name_score(name) * (index + 1)
        total_score += score

    return total_score


if __name__ == '__main__':
    result = solve()
    print(result)
