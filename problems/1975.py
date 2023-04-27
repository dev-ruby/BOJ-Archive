# 1975 - Number Game

import sys
from math import ceil


def solve():
    input = sys.stdin.readline

    def f(N, b) -> int:
        count = 0

        while True:
            if N % b == 0:
                count += 1
                N //= b
            else:
                break

        return count

    for _ in range(int(input())):
        n = int(input().strip())
        s = 0
        for i in range(2, ceil(n) + 1):
            s += f(n, i)

        print(s)


if __name__ == "__main__":
    solve()
