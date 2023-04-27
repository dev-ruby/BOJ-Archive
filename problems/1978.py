# 1978 - 소수 찾기

import sys


def is_prime_number(n):
    if n == 2:
        return True
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solve():
    input = sys.stdin.readline

    n = int(input())
    pl = map(int, input().split())
    c = 0
    for i in pl:
        if is_prime_number(i):
            c += 1
    print(c)


if __name__ == "__main__":
    solve()
