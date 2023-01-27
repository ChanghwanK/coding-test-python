def solution(arr):
    max_val_in_arr = max(arr)

    if len(arr) != max_val_in_arr:
        return False

    arr.sort()

    answers = [x for x in range(1, max_val_in_arr+1)]

    return arr == answers


print(solution([4, 1, 3, 2]))
