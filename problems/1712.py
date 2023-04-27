# 1712 - 손익분기점

import sys


def solve():
    input = sys.stdin.readline

    a, b, c = tuple(map(int, input().split()))

    if b >= c:
        print(-1)
    else:
        print(a // (c - b) + 1)


if __name__ == "__main__":
    solve()
