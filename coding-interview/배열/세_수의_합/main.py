from typing import List


def three_num_sum(nums: List[int]):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            # sum이 0이되는 첫 번째 케이스를 찾음
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum이 0이 되는 첫번째 순간임
                result.append([nums[i], nums[left], nums[right]])
                # left의 중복되는 숫자는 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # right 중복되는 숫자도 스킵
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result


print(three_num_sum([-1, 0, 1, 2, -1, -4]))
