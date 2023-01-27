def solution(arr):
    answer = True
    max_val_in_arr = max(arr)

    if len(arr) != max_val_in_arr:
        return False

    arr.sort()

    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False

    return answer


print(solution([4, 1, 3, 2]))
