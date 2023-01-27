
def bin_search(array: list, target: int) -> bool:
    array.sort()
    start: int = 0
    end: int = len(array) - 1

    while start <= end:
        mid: int = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


print("result: ", bin_search([1, 4, 3, 5, 2, 11, 7, 6], 6))
