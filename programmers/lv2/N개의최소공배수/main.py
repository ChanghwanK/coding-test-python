# n개의 수의 최소공배수는 n개의 수들의 배수 중 공통이되는 가장 작은 숫자

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b)//gcd(a, b)


def solution(arr):
    num = arr.pop(0)

    for value in arr:
        num = lcm(num, value)

    return num


print(solution([2, 6, 8, 14]))
