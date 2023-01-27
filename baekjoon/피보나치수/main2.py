import sys

N = int(sys.stdin.readline())

a, b = 0, 1

while N > 0:
    a, b = b, a + b
    N -= 1

print(a)
