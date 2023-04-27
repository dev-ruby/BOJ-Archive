# 1021 - 회전하는 큐

import sys
import collections


def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    deque = collections.deque(range(1, n + 1))
    nums = list(map(int, input().split()))
    count = 0

    for i in nums:
        while True:
            if deque[0] == i:
                deque.popleft()
                break
            else:
                if deque.index(i) < (len(deque) / 2):
                    while deque[0] != i:
                        deque.rotate(-1)
                        count += 1
                else:
                    while deque[0] != i:
                        deque.rotate(1)
                        count += 1
    print(count)


if __name__ == "__main__":
    solve()
