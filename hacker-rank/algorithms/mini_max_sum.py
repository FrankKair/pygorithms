#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/mini-max-sum/problem
from itertools import permutations


def mini_max_sum(arr):
    max_product = sum(max(permutations(arr, 4)))
    min_product = sum(min(permutations(arr, 4)))
    return (min_product, max_product)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    result = mini_max_sum(arr)
    print(result)
