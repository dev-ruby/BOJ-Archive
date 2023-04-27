# 1181 - 단어 정렬

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    word_list = list()

    for _ in range(N):
        word_list.append(input().rstrip("\n"))

    word_list = set(word_list)
    word_list = list(word_list)
    word_list.sort()
    word_list.sort(key=lambda x: len(x))

    for i in word_list:
        print(i)


if __name__ == "__main__":
    solve()
