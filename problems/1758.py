# 1758 - 알바생 강호

import sys


def solve():
    input = sys.stdin.readline

    N = int(input())

    n_list = list()
    money = 0

    for _ in range(N):
        n_list.append(int(input()))

    n_list.sort(key=lambda x: -x)

    for i in range(N):
        current = n_list[i] - i
        if current > 0:
            money += current

    print(money)


if __name__ == "__main__":
    solve()
