# 총 N의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함된 문자는 몇개인지?

import sys

N, M = map(int, sys.stdin.readline().split())

words_map = dict()
words = []

for _ in range(N):
    words_map[sys.stdin.readline()] = 0

for _ in range(M):
    words.append(sys.stdin.readline())


cnt = 0

for word in words:
    try:
        words_map[word]
        cnt += 1
    except KeyError:
        pass

print(cnt)
