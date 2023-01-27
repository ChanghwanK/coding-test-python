from typing import List

# end를 마지막부터 하느 방식


def two_pointer(nums: List[int], target):
    start = 0
    end = len(nums) - 1

    nums.sort

    while start < end:
        sum = nums[start] + nums[end]
        if sum < target:
            start += 1
        elif sum > target:
            end -= 1
        else:
            return [nums[start], nums[end]]

    return []


print(two_pointer([2, 7, 11, 15], 9))
