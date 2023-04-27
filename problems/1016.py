# 1016 - 제곱 ㄴㄴ 수

import sys
import math


def get_square_number(m, M):
    counted = [1] * (M - m + 1)

    i = 2

    while i**2 <= M:
        s = i**2
        mod = 0 if m % s == 0 else 1
        j = m // s + mod
        while s * j <= M:
            if counted[s * j - m] == 1:
                counted[s * j - m] = 0
            j += 1
        i += 1

    return sum(counted)


def solve():
    input = sys.stdin.readline
    m, M = map(int, input().split())

    print(get_square_number(m, M))


if __name__ == "__main__":
    solve()
