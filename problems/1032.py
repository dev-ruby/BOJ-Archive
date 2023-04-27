# 1032 - 명령 프롬프트

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    files = [sys.stdin.readline().strip() for _ in range(N)]

    file_name = list(files[0])
    legnth = len(file_name)
    if legnth == 1:
        if files.count(file_name[0]) != N:
            print("?")
            return
    for i in range(1, N):
        for j in range(legnth):
            if file_name[j] != files[i][j]:
                file_name[j] = "?"
    print("".join(file_name))


if __name__ == "__main__":
    solve()
