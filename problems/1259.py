# 1259 - 팰린드롬수

import sys


def solve():
    input = sys.stdin.readline
    while True:
        N = input()
        if N == "0":
            return
        if N[::-1] == N:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()
