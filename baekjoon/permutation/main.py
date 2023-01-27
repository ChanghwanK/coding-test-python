# 주어진 데이터로 만들 수 있는 숫자 중 두 자리 숫자에서 최댓값 찾기
data = [1, 2, 3, 4]
visit = [False] * len(data)
selected = list()


def recursive(idx):
    if idx == 2:
        print(selected)

        return

    for i in range(0, len(data)):
        if visit[i]:
            continue
        visit[i] = True
        selected.append(data[i])
        recursive(idx + 1)
        visit[i] = False
        selected.pop()


recursive(0)
