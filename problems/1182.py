# 1182 - 부분수열의 합

import sys
import itertools


def solve():
    input = sys.stdin.readline
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0

    for i in range(1, n + 1):
        for j in itertools.combinations(nums, i):
            if sum(j) == s:
                count += 1

    print(count)


if __name__ == "__main__":
    solve()
