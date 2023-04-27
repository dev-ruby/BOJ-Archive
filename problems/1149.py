# 1149 - RGB거리

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    n_list = list()

    for _ in range(N):
        n_list.append(list(map(int, sys.stdin.readline().split())))

    for i in range(1, N):
        n_list[i][0] = min(n_list[i - 1][1], n_list[i - 1][2]) + n_list[i][0]
        n_list[i][1] = min(n_list[i - 1][2], n_list[i - 1][0]) + n_list[i][1]
        n_list[i][2] = min(n_list[i - 1][1], n_list[i - 1][0]) + n_list[i][2]

    print(min(n_list[N - 1]))


if __name__ == "__main__":
    solve()
