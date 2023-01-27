# 문자열 배열을 받아 애너그램 단위로 그룹핑
from typing import List
import collections


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # 단어의 구성이 같다면 애너그램이라 볼 수 있음
    # 단어의 구성이 같다는 것은 정렬 했을 때의 값이 같다는 것을 의미
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
