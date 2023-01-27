import sys
input = sys.stdin.readline

mans = [int(input()) for _ in range(9)]
limit = len(mans)
total = sum(mans)

for i in range(0, limit):
    for j in range(i + 1, limit):
        if (total - mans[i] - mans[j]) == 100:
            for k in range(0, limit):
                if i == k or j == k:
                    continue
                print(mans[k])
            sys.exit(0)
