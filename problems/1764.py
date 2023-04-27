# 1764 - 듣보잡

import sys


def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    lst = []

    people = {}

    for _ in range(N):
        people[sys.stdin.readline().strip()] = 0

    for _ in range(M):
        name = sys.stdin.readline().strip()
        if people.get(name) == 0:
            lst.append(name)

    lst.sort()

    print(len(lst))

    print("\n".join(lst))


if __name__ == "__main__":
    solve()
