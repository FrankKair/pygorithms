#!/usr/bin/env python3


result = 0
for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a + b + c == 1000:
            result = a * b * c
            break


print(result)
