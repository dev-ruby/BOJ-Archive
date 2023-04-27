# 1110 - 더하기 사이클

import sys


def solve():
    input = sys.stdin.readline

    def number(x, y):
        return y + str(int(x) + int(y))[-1]

    N = input()
    if len(N) == 1:
        N = "0" + N
    n = 1
    new = number(N[0], N[1])
    while True:
        if new == N:
            break
        n = n + 1
        new = number(new[0], new[1])
    print(n)


if __name__ == "__main__":
    solve()
