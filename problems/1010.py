# 1010 - 다리 놓기

import sys
import math


def solve():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
        print(bridge)


if __name__ == "__main__":
    solve()
