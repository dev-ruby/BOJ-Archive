# 1546 - 평균

import sys


def solve():
    input = sys.stdin.readline

    n = int(input())
    scores = list(map(int, input().split()))
    M = max(scores)
    for i in range(n):
        scores[i] = scores[i] / M * 100
    avg = sum(scores) / n
    print(avg)


if __name__ == "__main__":
    solve()
