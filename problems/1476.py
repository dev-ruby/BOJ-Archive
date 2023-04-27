# 1476 - 날짜 계산

import sys


def solve():
    input = sys.stdin.readline

    e, s, m = map(int, input().split())
    e %= 15
    s %= 28
    m %= 19

    i = 1
    while True:
        if i % 15 == e and i % 28 == s and i % 19 == m:
            break
        i += 1
    print(i)


if __name__ == "__main__":
    solve()
