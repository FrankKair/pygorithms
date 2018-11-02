#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/camelcase/problem


def camel_case(s):
    return len([char for char in s if char.isupper()]) + 1


if __name__ == '__main__':
    s = 'saveChangesInTheEditor'
    result = camel_case(s)
    print(result)
