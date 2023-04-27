# 1932 - 정수 삼각형

import sys


def solve():
    input = sys.stdin.readline

    N = int(input())

    tri = []

    for _ in range(N):
        tri.append(list(map(int, sys.stdin.readline().split())))

    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                tri[i][j] += tri[i - 1][j]
                continue
            elif j == i:
                tri[i][j] += tri[i - 1][j - 1]
                continue
            else:
                tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1])
                continue
    print(max(tri[N - 1]))


if __name__ == "__main__":
    solve()
