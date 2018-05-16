#!/usr/bin/env python3
def primes():
    D = {}
    q = 2

    while True:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D:
                x += p
            D[x] = p
        else:
            D[q * q] = q
            yield q
        q += 1


def take_prime(n):
    for index, number in enumerate(primes()):
        if index == n - 1:
            return number


def solve():
    return take_prime(10001)

if __name__ == '__main__':
    result = solve()
    print(result)
