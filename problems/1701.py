# 1701 - Cubeditor

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


def solve():
    input = sys.stdin.readline

    T = input()
    res = 0

    for i in range(len(T)):
        sub = T[i:]
        res = max(max(get_pi(sub)), res)

    print(res)


if __name__ == "__main__":
    solve()
