# 1747 - 소수&팰린드롬

import sys

import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def solve():
    input = sys.stdin.readline

    N = int(input())

    for i in range(N, 1000001):
        if i == 1:
            continue
        if str(i) == str(i)[::-1]:
            if isPrime(i):
                print(i)
                return

    print(1003001)


if __name__ == "__main__":
    solve()
