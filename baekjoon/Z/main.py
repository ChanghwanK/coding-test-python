import sys

N, r, c = list(map(int, (sys.stdin.readline().split())))
result = 0


def recursive(n, x, y):
    global result

    if n == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1
        if x == r and y + 1 == c:
            print(result)
            return
        result += 1
        if x + 1 == r and y == c:
            print(result)
            return
        result += 1
        if x + 1 == r and y + 1 == c:
            print(result)
            return
        result += 1
        return

    recursive(n / 2, x, y)
    recursive(n / 2, x, y + n / 2)
    recursive(n / 2, x + n / 2, y)
    recursive(n / 2, x + n / 2, y + n / 2)


recursive(2 ** N, 0, 0)
