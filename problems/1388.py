# 1388 - 바닥 장식

import sys

sys.setrecursionlimit(100000)


def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    visited = [[False for _ in range(M)] for _ in range(N)]

    graph = []

    for _ in range(N):
        graph.append(list(input()))

    def dfs(n, m, pattern):
        nonlocal visited, N, M

        visited[m][n] = True

        if pattern == "-":
            if n + 1 == M:
                return
            elif not visited[m][n + 1] and graph[m][n + 1] == "-":
                dfs(n + 1, m, pattern)
            else:
                return
        elif pattern == "|":
            if m + 1 == N:
                return
            elif not visited[m + 1][n] and graph[m + 1][n] == "|":
                dfs(n, m + 1, pattern)
            else:
                return

    count = 0

    for y in range(N):
        for x in range(M):
            if not visited[y][x]:
                count += 1
                dfs(x, y, graph[y][x])

    print(count)


if __name__ == "__main__":
    solve()
