from typing import List

# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 반환


def two_sum(arr: List[int], target: int):
    # 2중 반복문으로 i기준으로 만들 수 있는 조합을 다 찾기
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

    return []


# result = two_sum([2, 7, 11, 15], 9)
# print(result)


def two_sum_2(arr: List[int], target: int):
    for i, n in enumerate(arr):
        complement = target - n

        if complement in arr[i + 1:]:
            return [arr.index(n), arr[i + 1:].index(complement) + (i+1)]


# result = two_sum_2([2, 7, 11, 15], 9)
# print(result)


def two_sum_3(arr: List[int], target: int):
    nums_map = {}

    for i, num in enumerate(arr):
        nums_map[num] = i

    # print(nums_map)  # key = elements,  value = index

    # target = i + j
    # target - i = j
    for i, num in enumerate(arr):
        # nums_map의 key들은 배열의 요소들이
        # 배열의 요소를 순회하지 않고 바로 key를 통해 존재 유무를 판단할 수 있음
        # and i != nums_map[target - num]: 왜 있는걸까
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

        return []


result = two_sum_3([2, 7, 11, 15], 9)
print(result)
