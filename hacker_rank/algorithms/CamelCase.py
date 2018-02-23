#!/usr/bin/env python3
import sys


def camelcase(s):
    return len([char for char in s if char.isupper()]) + 1


if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
