def solution(lines):
    arr = [0] * 200
    answer = 0
    for line in lines:
        x1 = line[0]
        x2 = line[1]
        for i in range(x1, x2):
            arr[i] += 1

    for num in arr:
        if num > 1:
            answer += 1
    return answer


print(solution([[0, 1], [2, 5], [3, 9]]))
