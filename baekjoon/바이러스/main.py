n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

arr = []

for i in range(m):
    arr.append(list(input().split()))


graph = {}


for value in arr:
    graph.setdefault(value[0], set(value[1]))
    graph[value[0]].add(value[1])

visit = []

print(graph)


def dfs(graph, start):
    visit.append(start)

    for node in graph[start]:
        if node not in visit:
            dfs(graph, node)


start = list(graph.keys())[0]
# dfs(graph, start)

# print(visit)
# print("size: ", len(visit))
