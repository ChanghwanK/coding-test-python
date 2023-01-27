# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.

n = int(input())
nums = [int(input()) for _ in range(0, n)]
stack = []
res = []
cnt = 1

for data in nums:
    while cnt >= data:
        stack.append(cnt)
        cnt += 1
        res.append('+')
    if stack[-1] == data:
        stack.pop()
        res.append('-')
    else:
        print('No')
        exit(0)

print('\n'.join(res))
