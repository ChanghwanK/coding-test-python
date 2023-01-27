from collections import Counter
from operator import itemgetter


def solution(array):
    nums = Counter(array)
    count_list = nums.items()
    mode = sorted(count_list, key=itemgetter(1), reverse=True)[0][0]
    count_frequcies = Counter(nums.values())

    return -1 if count_frequcies[nums[mode]] > 1 else mode


print(solution([1, 2, 3, 3, 3, 4]))
