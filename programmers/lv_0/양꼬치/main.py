def solution(n, k):
    price_a = 12000
    price_b = 2000
    temp = 1

    if n >= 10:
        temp = n // 10

    if k > 0:
        return (n * price_a) + (price_b * (k - temp))
    else:
        return (n * price_a)


print(solution(64, 6))
