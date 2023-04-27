# 1245 - 농장 관리

import sys

sys.setrecursionlimit(100000)


def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    is_peak = True
    count = 0

    for i in range(N):
        graph[i] = list(map(int, input().split()))

    def dfs(n, m):
        nonlocal visited, graph, is_peak, N, M
        try:
            visited[m][n] = True
        except:
            print(n, m)
            print(*visited, sep="\n")

        for x, y in (
            (n - 1, m - 1),
            (n - 1, m),
            (n - 1, m + 1),
            (n, m - 1),
            (n, m + 1),
            (n + 1, m - 1),
            (n + 1, m),
            (n + 1, m + 1),
        ):
            if (0 <= x < M) and (0 <= y < N):
                if graph[y][x] > graph[m][n]:
                    is_peak = False
                elif graph[y][x] == graph[m][n]:
                    if not visited[y][x]:
                        dfs(x, y)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] != 0:
                is_peak = True
                dfs(j, i)
                count += int(is_peak)

    print(count)


if __name__ == "__main__":
    solve()
