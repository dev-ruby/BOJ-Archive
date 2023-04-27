# 1158 - 요세푸스 문제

import sys
import collections


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    queue = collections.deque(list(range(1, N + 1)))
    perm = list()
    while queue:
        queue.rotate(-K + 1)
        perm.append(str(queue.popleft()))
    print(f"<{', '.join(perm)}>")


if __name__ == "__main__":
    solve()
