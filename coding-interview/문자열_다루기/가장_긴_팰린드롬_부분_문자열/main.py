# 주어진 문자에서 가장 긴 팰린드롬 문자를 찾는 것
def longest_palindrom(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # left가 0인 경우의 char가  right의 char와 같을 수 있기 때문에
        return s[left + 1: right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        # 탐색할 케이스가 2개이기 떄문에 expand를 두 번 사용함
        # 즉,
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print("result: " + longest_palindrom("babad"))
