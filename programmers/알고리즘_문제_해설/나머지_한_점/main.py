'''
    x1 x2는 가로 길이
    - y가 같은 것끼리
    y1 y2는 세로 길이
    - x가 같은 것끼리
'''


def solution(v):
    answer = []
    # 완성된 변 구하기
    x_arr = []
    y_arr = []

    for arr in v:
        x_arr.append(arr[0])
        y_arr.append(arr[1])

    # 필요한 좌표 구하기
    # 두 개가 아닌 것
    x_dict = {}
    y_dict = {}

    for x in x_arr:
        x_dict.setdefault(x, 0)
        x_dict[x] += 1

    for y in y_arr:
        y_dict.setdefault(y, 0)
        y_dict[y] += 1

    for key in x_dict.keys():
        if x_dict.get(key) == 1:
            answer.append(key)

    for key in y_dict.keys():
        if y_dict.get(key) == 1:
            answer.append(key)

    return answer


res = solution([[1, 4], [3, 4], [3, 10]])
print(res)
