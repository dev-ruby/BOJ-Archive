# 1157 - 단어 공부

import sys


def solve():
    input = sys.stdin.readline
    word = input().upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    c = 0
    a = ""
    for i in alphabet:
        if c == word.count(i):
            a = "?"
        if c < word.count(i):
            c = word.count(i)
            a = i
    print(a)


if __name__ == "__main__":
    solve()
