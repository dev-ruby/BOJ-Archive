# 1330 - 두 수 비교하기

import sys


def solve():
    input = sys.stdin.readline

    a, b = map(int, input().split())
    if a == b:
        print("==")
    elif a < b:
        print("<")
    elif a > b:
        print(">")


if __name__ == "__main__":
    solve()
