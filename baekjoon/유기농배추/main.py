import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs
# x,y 좌표를 받아서 방문

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def dfs(y, x):
    global visit

    if x < 0 or x >= N and y < 0 or y >= M:
        return

    if visit[y][x] or not field[y][x]:
        return

    visit[y][x] = True
    for idx in range(4):
        newY = y + dirR[idx]
        newX = x + dirC[idx]
        dfs(newY, newX)


    # 입력
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            print(field[i][j], end=' ')
        print()
    #         if field[i][j] and not visit[i][j]:
    #             dfs(i, j)
    #             ans += 1

    # print(ans)
