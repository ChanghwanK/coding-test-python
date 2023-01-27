
def rescursive(num: int) -> int:
    if num == 1:
        return num
    else:
        return num * rescursive(num - 1)


result = rescursive(5)
print(result)
