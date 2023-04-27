# 2023 - 신기한 소수

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
    if N == 1:
        return False
    if N in [2, 3, 5, 7, 9, 13, 17]:
        return True

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
    N = int(input())

    if N == 1:
        print("\n".join(["2", "3", "5", "7"]))
        return
    for i in range(10 ** (N - 1) + 1, 10**N):
        if i % 2 == 0 or i % 3 == 0:
            continue
        i_str = str(i)

        if (
            "2" in i_str[1:]
            or "4" in i_str[1:]
            or "6" in i_str[1:]
            or "8" in i_str[1:]
            or "0" in i_str[1:]
            or "5" in i_str[1:]
        ):
            continue

        if not is_prime(i):
            continue

        prime = True

        if not i_str[0] in ["2", "3", "5", "7"]:
            continue

        for i in range(1, N):
            if not is_prime(int(i_str[: N - i])):
                prime = False
                break

        if prime:
            print(i_str)


if __name__ == "__main__":
    solve()
