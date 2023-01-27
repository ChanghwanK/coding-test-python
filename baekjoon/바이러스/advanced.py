n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수


graph = [[] for i in range(n+1)]
visit = [0] * (n + 1)

# 인덱스가 key가 됨
for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

print("garph: ", graph)


def dfs(start):
    visit[start] = 1
    for node in graph[start]:
        if not visit[node]:
            dfs(node)


dfs(1)
print(sum(visit) - 1)
