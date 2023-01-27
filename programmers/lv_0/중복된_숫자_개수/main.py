def solution(array, n):
    answer = 0
    for num in array:
        if num == n:
            answer += 1
    return answer

result = solution([1,1,2,3,4,5], 1)

print("result: ", result)