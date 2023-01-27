from typing import List


def solution(absolutes: List[int], signs: List[bool]) -> int:
    # index로 순환
    total = 0

    for i in range(len(signs)):
        if signs[i]:
            total += absolutes[i]
        else:
            total -= absolutes[i]

    return total


print(solution([4, 7, 12], [True, False, True]))


def solution2(absolutes: List[int], signs: List[bool]) -> int:
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))


print(solution2([4, 7, 12], [True, False, True]))
