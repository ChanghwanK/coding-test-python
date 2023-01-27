# 구멍이 뚫려 있는 부부은 0
# 칸막이는 1
# 얼음 틀의 모양이 주어졌을 때 총 아이스크림의 개수를 구하시오
# case
'''
4 5
00110
00011
11111
00000
'''

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 총 몇개의 구역인가?
# 구역은 방문 할 수 있다면 근처를 모두 방문 처리하고
# 다시 그래프를 탐색하다 방문할 수 있다면 cnt 를 증가하면 됨


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x - 1, y - 1)
        dfs(x + 1, y)
        dfs(x, y+1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)
