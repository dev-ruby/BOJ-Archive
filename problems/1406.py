# 1406 - 에디터

import sys


def solve():
    input = sys.stdin.readline

    stack_A, stack_B = list(sys.stdin.readline().strip()), list()

    N = int(input())
    for _ in range(N):
        command = sys.stdin.readline().strip().split()
        if command[0] == "L":
            if stack_A:
                stack_B.append(stack_A.pop())

        elif command[0] == "D":
            if stack_B:
                stack_A.append(stack_B.pop())

        elif command[0] == "B":
            if stack_A:
                stack_A.pop()

        elif command[0] == "P":
            stack_A.append(command[1])

    print("".join(stack_A + list(stack_B)[::-1]))


if __name__ == "__main__":
    solve()
