# 1011 - Fly me to the Alpha Centauri

import sys


def solve():
    input = sys.stdin.readline
    r = int(input())

    for _ in range(r):
        x, y = map(int, input().split())
        d = y - x

        n = 0

        while True:
            if d <= n * (n + 1):
                break
            n += 1
        if d <= n**2:
            print(n * 2 - 1)
        else:
            print(n * 2)


if __name__ == "__main__":
    solve()
