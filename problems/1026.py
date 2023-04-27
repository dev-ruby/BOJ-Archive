# 1026 - 보물

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort(key=lambda x: -x)
    B_list.sort()

    s = 0

    for i in range(N):
        s += A_list[i] * B_list[i]

    print(s)


if __name__ == "__main__":
    solve()
