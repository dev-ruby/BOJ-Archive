# 1920 - 수 찾기

import sys


def solve():
    input = sys.stdin.readline

    N = int(sys.stdin.readline().strip())
    n_list = list(map(int, sys.stdin.readline().strip().split()))
    n_list.sort()

    M = int(sys.stdin.readline().strip())
    m_list = map(int, sys.stdin.readline().strip().split())

    def search(i):
        start = 0
        end = len(n_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if n_list[mid] == i:
                print("1")
                return
            elif n_list[mid] < i:
                start = mid + 1
            else:
                end = mid - 1
        print("0")
        return

    for i in m_list:
        search(i)


if __name__ == "__main__":
    solve()
