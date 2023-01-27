import math


def solution(progresses, speeds):
    answer = []
    need_days = []
    # 필요한 일 수 구하기
    # 93 30 55
    for i in range(len(progresses)):
        need_days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # 7 3 9
    # 더 작은 값들 개수 카운팅

    # 필요한 일 수 구하기
    cnt = 1
    first_day = need_days.pop(0)
    print(first_day)
    while (need_days):
        day = need_days.pop(0)
        if (first_day >= day):
            cnt += 1
            continue

        answer.append(cnt)
        cnt = 1
        first_day = day
    answer.append(cnt)
    return answer


ans = solution([93, 30, 55], [1, 30, 5])
print("result: ", ans)
