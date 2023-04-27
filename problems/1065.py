# 1065 - 한수

import sys


def solve():
    input = sys.stdin.readline
    n = int(input())
    count = 0

    def han(i):
        if i < 100:
            return True
        i_list = list(map(int, list(str(i))))
        d = i_list[1] - i_list[0]
        for n in range(len(i_list)):
            if n == 0:
                continue
            if not (i_list[n] - i_list[n - 1] == d):
                return False
        return True

    for i in range(1, n + 1):
        if han(i):
            count += 1
    print(count)


if __name__ == "__main__":
    solve()
