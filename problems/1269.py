# 1269 - 대칭 차집합

import sys


def solve():
    input = sys.stdin.readline

    input()
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    print(len(a - b) + len(b - a))


if __name__ == "__main__":
    solve()
