# 1966 - 프린터 큐

import sys


def solve():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().strip().split())
        n_list = list(map(int, sys.stdin.readline().strip().split()))
        count = 0
        while True:
            if max(n_list) != n_list[0]:
                if M == 0:
                    M = len(n_list)
                n_list.append(n_list.pop(0))
            else:
                count += 1
                if M == 0:
                    break
                n_list.pop(0)
            M -= 1
        print(count)


if __name__ == "__main__":
    solve()
