
# 주어진 숫자 배열이 오름차순인지 내림차순인지

# 이전 값보다 계속 작다면 내림차순
# 이전 값보다 계속 크다면 오름차순
# 둘 다 아니면 그렇지도 않다면 MIX

asc = True
desc = True
mixed = True

# nums = [int(input()) for _ in range(8)]
nums = list(map(int, input().split()))


for i in range(0, len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            asc = False
        elif nums[i] < nums[j]:
            desc = False
        else:
            mixed = False

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')
