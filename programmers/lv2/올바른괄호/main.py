'''
stack이 비었다면 append
stack이 비었지 않다면 체크

체크 내용
- ( 이면 넣고 )이면 pop
'''


def solution(s):
    stack = []
    for braket in s:
        if stack:
            if braket == "(":
                stack.append(braket)
            else:
                stack.pop()
        else:
            stack.append(braket)
    return len(stack) == 0


print(solution("()()"))
