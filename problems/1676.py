# 1676 - 팩토리얼 0의 개수

import sys
import math


def solve():
    input = sys.stdin.readline

    N = int(input())
    count = 0

    f = str(math.factorial(N))[::-1]

    for i in range(len(f)):
        if f[i] == "0":
            count += 1
        else:
            break

    print(count)


if __name__ == "__main__":
    solve()
