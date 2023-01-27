# 현재 맵을 방문하지 않았다면 방문할 것
# 방문 할 때 최소 피로도를 충족하는지 검사
# 현재 턴에서 방문 했다면 다른 턴에서도 방문할 수 있도록 false처리

ans = 0


def dfs(idx: int, pirodo: int, dugeons: list, visit: list):
    global ans
    if idx == len(dugeons):
        return

    for i in range(len(dugeons)):
        if not visit[i] and dugeons[i][0] <= pirodo:
            visit[i] = True
            dfs(idx + 1, pirodo - dugeons[i][1], dugeons, visit)
            visit[i] = False

    ans = max(idx, ans)


def solution(k, dungeons):
    visit = [False] * len(dungeons)
    dfs(0, k, dungeons, visit)
    return ans
