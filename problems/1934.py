# 1934 - 최소공배수

import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())
        print(a * b // gcd(a, b))


if __name__ == "__main__":
    solve()
