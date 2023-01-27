import sys
N = sys.stdin.readline()
sag_cards = list(map(int, sys.stdin.readline().split(" ")))
M = sys.stdin.readline()
cards = list(map(int, sys.stdin.readline().split(" ")))
sangen_card_map = {}
ans = []

for card in sag_cards:
    sangen_card_map[card] = 0

for card in cards:
    res = sangen_card_map.get(card)
    if not res is None:
        ans.append("1")
    else:
        ans.append("0")


print(" ".join(ans))
