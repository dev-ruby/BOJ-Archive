# 1085 - 직사각형에서 탈출

import sys


def solve():
    input = sys.stdin.readline
    x, y, w, h = map(int, input().split())
    print(min((w - x, x, h - y, y)))


if __name__ == "__main__":
    solve()
