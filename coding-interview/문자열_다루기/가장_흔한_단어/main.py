# 금지된 단어를 제외하고 가장 흔한 단어 출력
import collections
import re
from typing import List


def most_commond_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(
        r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


result = most_commond_word(
    paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"])
print("result: " + result)
