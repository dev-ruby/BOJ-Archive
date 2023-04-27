# 1427 - 소트인사이드

import sys


def solve():
    input = sys.stdin.readline

    N = list(map(int, list(input())))

    N.sort()

    N = list(map(str, N))

    print("".join(N[::-1]))


if __name__ == "__main__":
    solve()
