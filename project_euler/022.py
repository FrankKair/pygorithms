#!/usr/bin/env python3
import os


def name_score(name):
    """
    chr('65') >>> 'A'
    chr('97') >>> 'a'
    97 - 65 = 32
    """
    score = 0
    for char in name:
        score += ord(char) % 32
    return score


def remove_quotes(string):
    return string.strip('\"')


def names():
    file = open(os.path.join(os.path.dirname(__file__), 'p022_names.txt'))
    return sorted(file.read().split(','))


names_list = names()

total_score = 0
for index, name in enumerate(names_list):
    name = remove_quotes(name)
    score = name_score(name) * (index + 1)
    total_score += score

print(total_score)
