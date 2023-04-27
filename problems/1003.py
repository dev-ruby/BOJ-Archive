# 1003 - 피보나치 함수

import sys


def fibo(N):
    dp = [[0, 0]] * (max(N) + 1)
    if max(N) < 2:
        if max(N) == 0:
            print("1 0")
            return
        elif max(N) == 1:
            print("0 1")
            return
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, max(N) + 1):
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

    for i in N:
        print(" ".join(map(str, dp[i])))
        pass


def solve():
    input = sys.stdin.readline
    N = int(input())

    n_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

    fibo(n_list)


if __name__ == "__main__":
    solve()
