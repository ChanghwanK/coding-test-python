# 입력
import sys
from collections import defaultdict
input = sys.stdin.readline

s1, s2, s3 = list(map(int, input().split()))

# 주사위 초기화
dice_01 = [x for x in range(1, s1 + 1)]
dice_02 = [x for x in range(1, s2 + 1)]
dice_03 = [x for x in range(1, s3 + 1)]

# 합 구하고 dict에 push
total = 0
score_dict = defaultdict(int)

for i in range(len(dice_01)):
    for j in range(len(dice_02)):
        for k in range(len(dice_03)):
            total = dice_01[i] + dice_02[j] + dice_03[k]
            score_dict[total] += 1

# dict 정렬
sorted_dict = sorted(score_dict.items(),
                     key=lambda item: item[1], reverse=True)
# print(sorted_dict)

# # 출력
print(sorted_dict[0][0])
