# AEIOU만을 사용하여 만들 수 있는 길이 5이하의 모든 단어가 수록되어있음
# word는 몇번째 단어인가?

combo = []
AEIOU = ["A", "E", "I", "O", "U"]


def comb(char: str, idx):
    if char:
        combo.append(char)

    if idx == len(AEIOU):
        return

    for i in range(len(AEIOU)):
        comb(char + AEIOU[i], idx + 1)


def solution(word):
    answer = 0
    # AEIOU를 사용해서 만들 수 있는 모든 단어를 만듬
    comb("", 0)

    answer = combo.index(word) + 1
    # 주어진 단어는 몇번째 단어인지 체크
    return answer


result = solution("AAAAE")
print(result)
