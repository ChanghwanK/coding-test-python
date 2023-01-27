
def binary_search(nums: list, target: int):
    start: int = 0
    end: int = len(nums) - 1
    mid: int = 0

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            print("Found It!!")
            return
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    print("None")


binary_search([1, 2, 3, 4, 5, 6, 7], 9)
