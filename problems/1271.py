# 1271 - 엄청난 부자2

import sys


def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    print("\n".join(map(str, divmod(N, M))))


if __name__ == "__main__":
    solve()
