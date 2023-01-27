def solution(babblings: list):
    # 최대한 번씩만 조합해서 사용할 수 있음
    cnt: int = 0
    can_babblings: list = ["aya", "ye", "woo", "ma"]
    # babbling 문자가 읽을 수 있는지 판단
    for i in range(len(babblings) - 1):
        # 한 번만 발음 할 수 있기 때문에 두 번으로 이루어진 친구들은 건너 뜀
        if "ayaaya" in babblings[i] or "yeye" in babblings[i] or "woowoo" in babblings[i] or "mama" in babblings[i]:
            continue
        # 발음 할 수 있다는 것은 nword를 replace했을 때 replae 된 문자열로만 변경된다는 것을 의미함
        if babblings[i] in can_babblings[i]:
            babblings[i] = babblings[i].replace(can_babblings[i], '.')

    for ba in babblings:
        if ba is '.':
            cnt += 1
        if ba is "..":
            cnt += 1
        if ba is "...":
            cnt += 1
        if ba is "....":
            cnt += 1

    return cnt


if __name__ == '__main__':
    result = solution(["aya", "yee", "u", "maa", "wyeoo"])
    print(result)

    # str_1 = "ch"
    # str_2 = "changhwan"
    #
    # if str_2 in str_1:
    #     print("1. YES")
    #
    # if str_1 in str_2:
    #     print("2. YES")
