#!/usr/bin/env python3
from math import sqrt
from itertools import permutations


def list_primes_below(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(sqrt(n) + 1)):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


def solve():
	primes = list_primes_below(999999)
	
	def is_circular_prime(n):
		s = str(n)
		return all(primes[int(s[i : ] + s[ : i])] for i in range(len(s)))
	
	return sum(1 for i in range(len(primes)) if is_circular_prime(i))


if __name__ == '__main__':
    result = solve()
    print(result)
