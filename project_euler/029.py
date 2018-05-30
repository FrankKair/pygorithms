#!/usr/bin/env python3
def solve():
    # Generates set of a ^ b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100
    return len({a**b for a in range(2, 101) for b in range(2, 101)})


if __name__ == '__main__':
    result = solve()
    print(result)
