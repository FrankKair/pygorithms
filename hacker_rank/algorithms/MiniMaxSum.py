#!/usr/bin/env python3
import sys
from itertools import permutations


def miniMaxSum(arr):
    max_product = sum(max(permutations(arr, 4)))
    min_product = sum(min(permutations(arr, 4)))
    print(min_product, max_product)


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
