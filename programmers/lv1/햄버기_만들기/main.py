
# 빵 -> 야채 -> 고기 -> 빵 순으로 버거 만들어야 함
# 1: 빵 2: 야채 3: 고기
# 주어진 배열에서 햄버거를 몇개 만들 수 있는지?
# [2, 1, 1, 2, 3, 1, 2, 3, 1]
# 1 2 3 1 조합이 몇개 가능한지?
def solution(ingredient):
    answer = 0
    stack = list()
    # 1 2 3 1 배열이 있다면 제거하는 방식으로
    for i in ingredient:
        stack.append(i)

        if len(stack) >= 4 and stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1:
            for _ in range(4):
                stack.pop()
            answer += 1
    return answer


result = solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
print("result: ", result)
