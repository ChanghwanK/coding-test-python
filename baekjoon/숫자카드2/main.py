import sys
from collections import defaultdict
input = sys.stdin.readline


ans = []

n = int(input())
s_cards = list(map(int, input().split(" ")))
m = int(input())
g_cards = list(map(int, input().split(" ")))

s_cards_dict = defaultdict(int)

for card in s_cards:
    s_cards_dict[card] += 1


for card in g_cards:
    if card in s_cards_dict:
        ans.append(str(s_cards_dict.get(card)))
    else:
        ans.append("0")


print(" ".join(ans))
