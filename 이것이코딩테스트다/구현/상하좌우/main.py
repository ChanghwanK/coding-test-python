'''
구현해야할 것
N x N 크기의 정사각형 공간이 존재
상하좌우 방향으로 이동할 수 있는데 시작좌표는 항상 1, 1에서 시작 
계획서가 주어졌을 때 여행가의 마지막 위치는? 
'''

n = int(input())
commands = input().split()

x = 1
y = 1

while commands:
    command = commands.pop(0)
    if command == 'R':
        if not y + 1 == n:
            y += 1
    elif command == 'L':
        if not y - 1 == 0:
            y -= 1
    elif command == 'D':
        if not x + 1 == n:
            x += 1
    elif command == 'U':
        if not x - 1 == 0:
            x -= 1

print(str(x) + " " + str(y))
