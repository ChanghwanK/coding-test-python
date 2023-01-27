# 주어진 문자열이 팰린드롬인지 확인 대소문자는 구분하지 않음

from collections import deque
import re


def is_palindrom(word: str) -> bool:
    word = word.lower()
    pure_words = list()

    for a in word:
        if a.isalpha():
            pure_words.append(a)

    while len(pure_words) > 1:
        if pure_words.pop(0) != pure_words.pop():
            return False

    return True


print("result: ", is_palindrom("A man, a plan, a canal: Panama"))


def is_palindrom_using_deque(word: str) -> bool:
    word = word.lower()
    pure_words = deque()

    for char in word:
        if char.isalpha():
            pure_words.append(char)

    while len(pure_words) > 1:
        if pure_words.popleft() != pure_words.pop():
            return False
    return True


def is_palindrom_using_sub_string(word: str) -> bool:
    word = word.lower()

    word = re.sub("[^a-z0-9]", "", word)  # 숫자나 소문자가 아니라면 공백으로 치환

    return word == word[::-1]


print("result3: ", is_palindrom_using_sub_string(
    "A man, a plan, a canal: Panama"))
