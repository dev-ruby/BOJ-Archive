# 1990 - 소수인팰린드롬

import sys


def power(x, y, m):
    res = 1
    x = x % m
    while y > 0:
        if y & 1:
            res = (res * x) % m
        y = y >> 1
        x = (x * x) % m
    return res


def miller_rabin(n, a):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d // 2
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for i in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False


def is_prime(N):
    if N < 1373653:
        for i in [2, 3]:
            if not miller_rabin(N, i):
                return False
    elif N < 9080191:
        for i in [31, 73]:
            if not miller_rabin(N, i):
                return False
    else:
        for i in [2, 7, 61]:
            if not miller_rabin(N, i):
                return False
    return True


def solve():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 3 == 0:
            if i == 2 or i == 3:
                print(i)
            continue
        i_str = str(i)
        if len(i_str) % 2 == 0:
            if i == 11:
                print(i)
            continue
        if i_str == i_str[::-1]:
            if is_prime(int(i_str)):
                print(i_str)
    print(-1)


if __name__ == "__main__":
    solve()
