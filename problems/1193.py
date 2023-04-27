# 1193 - 분수찾기

import sys


def solve():
    input = sys.stdin.readline
    x = int(input())
    n = 1
    a = 0
    b = 0
    while True:
        a = n * (n + 1) / 2
        if a == x:
            break
        elif a > x:
            break
        elif a < x:
            n += 1
            continue

    if n % 2 == 1:
        a = 1 + (n * (n + 1) / 2 - x)

        b = n - (n * (n + 1) / 2 - x)

    else:
        a = n - (n * (n + 1) / 2 - x)
        b = 1 + (n * (n + 1) / 2 - x)
    a, b = map(int, (a, b))
    print(f"{a}/{b}")


if __name__ == "__main__":
    solve()
