# 1475 - 방 번호

import sys
import collections


def solve():
    input = sys.stdin.readline

    n = input()
    counter = collections.Counter(n)

    count = 0

    for n, c in counter.items():
        if n == "6" or n == "9":
            count = max(count, sum(list(divmod(counter["6"] + counter["9"], 2))))
        else:
            count = max(count, c)

    print(count)


if __name__ == "__main__":
    solve()
