# 1654 - 랜선 자르기

import sys


def solve():
    input = sys.stdin.readline

    K, N = map(int, input().split())
    n_list = list()
    for _ in range(K):
        n_list.append(int(input().strip()))

    high, low = sum(n_list) // N, 1  # 각 랜선의 최소/최대 길이
    while low <= high:
        mid = (high + low) // 2  # 최소/최대 중간값
        count = sum([x // mid for x in n_list])  # ?
        if count < N:
            high = mid - 1
        elif count >= N:
            low = mid + 1
            ans = mid
    print(ans)


if __name__ == "__main__":
    solve()
