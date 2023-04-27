# 1620 - 나는야 포켓몬 마스터 이다솜

import sys


def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    n_list = list()
    n_dict = dict()
    m_list = list()

    for i in range(N):
        data = sys.stdin.readline().strip()
        n_list.append(data)
        n_dict[data] = i

    for _ in range(M):
        m_list.append(sys.stdin.readline().strip())

    for i in m_list:
        if i.isdigit():
            print(n_list[int(i) - 1])
        else:
            print(n_dict[i] + 1)


if __name__ == "__main__":
    solve()
