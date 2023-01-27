x, y, w, h = list(map(int, input().split(" ")))

# 즉, 현 위치가 가로 세로 절반보다 더 크다면 우측 꼭짓점으로 작다면 좌측 꼭짓점으로 거리를 계산

x_mid = w / 2
y_mid = h / 2
res_1 = 0
res_2 = 0

if x > x_mid:
    # 우측으로 이동
    res_1 = w - x
else:
    res_1 = x - 0

if y > y_mid:
    res_2 = h - y
else:
    res_2 = y - 0


print(min(res_1, res_2))

#   7

#   1 2
#   4 5 6
