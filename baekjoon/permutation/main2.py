data = [1, 2, 3, 4]
visit = [False] * len(data)
num_map = list()


def recursive(num, idx):
    if num:
        num_map.append(num)

    if idx == len(data):
        return

    for i in range(len(data)):
        if visit[i]:
            continue
        visit[i] = True
        recursive(num + str(data[i]), idx+1)
        visit[i] = False


recursive("", 0)

print(num_map)
