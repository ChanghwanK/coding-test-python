N = int(input())
paper = [[0] * 101 for i in range(101)]

for _ in range(N):
    a, b = list(map(int, input().split()))
    for i in range(10):
        for j in range(10):
            paper[a + i][b + j] = 1

cnt = 0

for num in paper:
    cnt += sum(num)

print(cnt)
