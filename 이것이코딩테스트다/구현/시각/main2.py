'''
00시 00분 00초부터 Ntl 59분 59초까지의 모든 시각 중에서 하나라도 3이 포함되는
모든 경우의 수를 출력
'''
N = int(input())

si = 0
bun = 0
cho = 0

while bun != 60:
    bun += 1
    if bun == 60:
        si += 1
        if (si == N):
            break
        bun = 1
    while cho != 60:
        cho += 1
        print(str(si) + "시" + " " + str(bun) + "분" + " " + str(cho) + "초")
    cho = 1
