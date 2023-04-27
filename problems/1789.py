# 1789 - 수들의 합

import sys


def solve():
    input = sys.stdin.readline

    S = int(input())
    c = 0
    while True:
        if 0 == S:
            break
        if 0 > S:
            c -= 1
            break

        S -= c
        c += 1

    print(c - 1)


if __name__ == "__main__":
    solve()
