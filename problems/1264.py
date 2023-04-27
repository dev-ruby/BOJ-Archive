# 1264 - 모음의 개수

import sys


def solve():
    input = sys.stdin.readline

    while True:
        word = input()
        if word == "#":
            break
        else:
            print(sum([(int(ch in ["a", "e", "o", "u", "i"])) for ch in word.lower()]))


if __name__ == "__main__":
    solve()
