# 1874 - 스택 수열

import sys


def solve():
    input = sys.stdin.readline

    stack = list()
    N = int(input())
    count = 0
    n_list = list()
    pm = list()
    for _ in range(N):
        n_list.append(int(sys.stdin.readline().strip()))
    for i in n_list:
        while count < i:
            count += 1
            stack.append(count)
            pm.append("+")
        if stack[-1] == i:
            stack.pop()
            pm.append("-")
        else:
            print("NO")
            return
    for i in pm:
        print(i)


if __name__ == "__main__":
    solve()
