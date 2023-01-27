def solution(dartResult):
    power = {'S': 1, 'D': 2, 'T': 3}
    scores = []
    start_idx = 0

    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in power:
            scores.append(int(dartResult[start_idx:i]) ** power[op])
        elif op == '*':
            scores[-2:] = [x * 2 for x in scores[-2:]]
        elif op == '#':
            scores[-1:] = -scores[-1]

        if not op.isnumeric():
            start_idx = i + 1

    return sum(scores)
