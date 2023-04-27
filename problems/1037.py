# 1037 - 약수

import sys


def solve():
    input = sys.stdin.readline
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    print(n_list[0] * n_list[-1])


if __name__ == "__main__":
    solve()
