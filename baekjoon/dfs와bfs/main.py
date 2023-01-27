
# def dfs(idx):
#     global visited
#     visited[idx] = True
#     print(idx, end=' ')
#     for next in range(1, N + 1):
#         if not visited[next] and graph[idx][next]:
#             dfs(next)

def dfs(idx):
    global visited
    if not visited[idx]:
        print(idx, end=' ')
        visited[idx] = True
        for next in range(N + 1):
            if graph[idx][next]:
                dfs(next)


def bfs(start):
    global visited
    q = [start]
    visited[start] = True

    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


N, M, start = map(int, input().split(" "))

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split(" "))
    graph[x][y] = 1
    graph[y][x] = 1

dfs(start)
print()

visited = [False] * (N + 1)
bfs(start)
