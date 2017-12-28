#!/usr/bin/env python3
def square(number):
    return number * number


squared_sum = sum([square(x) for x in range(0, 101)])
square_of_the_sum = square(sum([x for x in range(0, 101)]))

result = square_of_the_sum - squared_sum

print(result)