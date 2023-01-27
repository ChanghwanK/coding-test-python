def solution(arr):
    answer = []
    # answer의 마지막 값과 들어갈 num과 같은지 비교 같다면 못넣고 같지 않다면 append
    for num in arr:
        if not answer:
            answer.append(num)
        else:
            if answer[len(answer) - 1] == num:
                continue
            else:
                answer.append(num)

    return answer


# print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
