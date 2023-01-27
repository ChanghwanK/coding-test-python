import sys
n, m = map(int, input().split())
visit = [False] * (n+1)
selected = [0] * m


def go(index):
    if index == m:
        sys.stdout.write(' '.join(map(str, selected))+'\n')
        return
    for i in range(1, n + 1):
        if visit[i]:
            continue
        visit[i] = True
        selected[index] = i
        go(index+1)
        visit[i] = False


go(0)
