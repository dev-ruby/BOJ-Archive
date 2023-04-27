# 1699 - 제곱수의 합

import sys
import random
from math import sqrt
from collections import Counter


def pow(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def miller_rabin(N, a):
    r = 0
    d = N - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    x = pow(a, d, N)
    if x == 1 or x == N - 1:
        return True

    for i in range(r - 1):
        x = pow(x, 2, N)
        if x == N - 1:
            return True
    return False


def is_prime(N):
    prime_list = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    if N == 1:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0:
        return False
    for a in prime_list:
        if N == a:
            return True
        if not miller_rabin(N, a):
            return False
    return True


def pollardRho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = ((x**2 % n) + c + n) % n
        y = ((y**2 % n) + c + n) % n
        y = ((y**2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollardRho(n)
    if is_prime(d):
        return d
    else:
        return pollardRho(d)


def legendre(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 == 7


def three_square(n):
    lst = []
    while n > 1:
        divisor = pollardRho(n)
        lst.append(divisor)
        n //= divisor

    c = list(Counter(lst).items())
    for i, n in c:
        if i % 4 == 3 and n % 2 == 1:
            return True
    return False


def solve():
    input = sys.stdin.readline

    N = int(input())

    if legendre(N):
        return 4
    elif three_square(N):
        return 3
    elif int(sqrt(N)) ** 2 != N:
        return 2
    else:
        return 1


if __name__ == "__main__":
    solve()
