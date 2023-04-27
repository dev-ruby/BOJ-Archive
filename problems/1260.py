# 1260 - DFS와 BFS

import sys

import collections


def solve():
    input = sys.stdin.readline

    N, M, V = map(int, input().split())

    graph = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = True
        graph[b][a] = True

    dfs_result = []
    bfs_result = []

    def dfs(v):
        visited[v] = True
        dfs_result.append(str(v))

        for i in range(1, N + 1):
            if (not visited[i]) and graph[v][i]:
                dfs(i)

    def bfs(v):
        queue = collections.deque([v])
        visited[v] = True

        while queue:
            v = queue.popleft()
            bfs_result.append(str(v))
            for i in range(1, N + 1):
                if (not visited[i]) and graph[v][i]:
                    queue.append(i)
                    visited[i] = True

    dfs(V)
    visited = [False for _ in range(N + 1)]
    bfs(V)

    print(" ".join(dfs_result))
    print(" ".join(bfs_result))


if __name__ == "__main__":
    solve()
