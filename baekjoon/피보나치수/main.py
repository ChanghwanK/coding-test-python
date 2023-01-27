# Fn = Fn-1 + Fn-2
import sys

# 입력
N = int(sys.stdin.readline())
# Fibo 0 = 0
# Fibo 1 = 1
# Fib0 2 = Fibo0 + Fibo1
# Fibo 3 = Fibo2 + Fibo 1


def fibo(n: int):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


print(fibo(N))
