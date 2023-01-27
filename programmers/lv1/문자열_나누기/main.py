# 첫 글자를 X
# x와 x가 아닌 다른 글자들이 나온 횟수를 각각 센다
# 처음으로 두 횟수가 같아지는 순간 멈추고 지금까지 읽은 문자열을 분리한다.
# s에서 분리한 문자열을 빼고 남은 부분을 위 과정을 반복한다.
# 남은 부분이 없다면 종료한다.
# 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면 지금까지 읽은 문자열을 분리하고 종료한다.

def solution(s: str):
    disintegrate_words = list()
    answer = 0
    x = s[0]
    x_equals_cnt = 0
    x_not_equals_cnt = 0

    for word in s:
        if word is x:
            x_equals_cnt += 1
        else:
            x_not_equals_cnt += 1

    return answer


solution("banana")
