import sys
S = input()

# 문자에서 영역을 파악 후 뒤집으면 됨
zero_area_cnt = 0
one_area_cnt = 0

start_word = S[0]
# 문자가 한 칸만 다른경우 검사

cnt = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        cnt += 1

if cnt == 1:
    print("1")
    sys.exit()

for i in range(1, len(S)):
    # 한 칸 한 칸 나아가면서 이전 값과 다른지 체크
    # 마지막 영역이 카운팅 안됨
    # 100100
    if start_word == '0':
        if S[i] != start_word:
            zero_area_cnt += 1
            start_word = '1'
    elif start_word == '1':
        if S[i] != start_word:
            one_area_cnt += 1
            start_word = '0'

if start_word == '0':
    zero_area_cnt += 1
else:
    one_area_cnt += 1

print(min(zero_area_cnt, one_area_cnt))
