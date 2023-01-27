
'''
1.  마지막 순열 찾기 i - 1
2.  마지막 순열에서 최소값 j 찾기
3.  i - 1, j swap
4.  i, j까지 다시 swap
'''


def next_permutation(arr: list):
    i = len(arr) - 1

    # i 구하기
    while i > 0 and arr[i - 1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    # j 구하기
    j = len(arr) - 1

    while arr[j] <= arr[j - 1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[j-1]

    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
