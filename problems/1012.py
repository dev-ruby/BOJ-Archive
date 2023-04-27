# 1012 - 유기농 배추

import sys

sys.setrecursionlimit(100000)


def solve():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    visited = [[False for _ in range(N)] for _ in range(M)]

    graph = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        n, m = map(int, input().split())
        graph[m][n] = 1

    houses = []

    count = 0

    current_houses = 0

    def dfs(n, m):
        nonlocal visited, count, current_houses, houses

        visited[m][n] = True

        current_houses += 1

        for x, y in ([n - 1, m], [n + 1, m], [n, m + 1], [n, m - 1]):
            try:
                cond = not visited[y][x] and graph[y][x] == 1
                if min(x, y) < 0:
                    cond = -1
            except:
                cond = -1
            if cond:
                if cond != -1:
                    dfs(x, y)

    for i in range(N):
        for j in range(M):
            if not visited[j][i] and graph[j][i] == 1:
                current_houses = 0
                dfs(i, j)
                houses.append(current_houses)
                count += 1

    print(count)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
