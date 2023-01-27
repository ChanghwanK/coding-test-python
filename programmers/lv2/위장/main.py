def solution(clothes):
    clothes_map = {}
    ans = 1

    for cl in clothes:
        key = cl[1]
        clothes_map.setdefault(key, [cl[0]])
        clothes_map[key].extend([cl[0]])

    for value in clothes_map.values():
        ans *= len(value)

    return ans - 1


result = solution([["yellow_hat", "headgear"], [
                  "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
