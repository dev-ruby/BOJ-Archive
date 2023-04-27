# 1786 - 찾기

import sys


def get_pi(pattern):
    pi = [0 for _ in range(len(pattern))]

    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i

    return pi


def kmp(data, pattern):
    pi = get_pi(pattern)

    res = []
    i = 0

    for j in range(len(data)):
        while i > 0 and pattern[i] != data[j]:
            i = pi[i - 1]
        if pattern[i] == data[j]:
            i += 1
            if i == len(pattern):
                res.append(j - i + 1)
                i = pi[i - 1]

    return res


def solve():
    input = sys.stdin.readline

    T = input()
    P = input()

    result = kmp(T, P)

    print(len(result))
    print(*map(lambda x: x + 1, result), sep=" ")


if __name__ == "__main__":
    solve()
