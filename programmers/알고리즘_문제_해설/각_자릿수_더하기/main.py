# 자연수 N이 주어지면 N의 각 자릿수의 합을 구해서 Return
def solution(n):
    answer = 0
    str_n = str(n)

    for num in str_n:
        answer += int(num)

    return answer
