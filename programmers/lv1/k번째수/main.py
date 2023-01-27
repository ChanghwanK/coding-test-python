
# 배열에서 i ~ j번째 숫자까지 자르고 정렬했을 때 k번째에 있는 수를 구하기
def solution(array, commands):
    answer = []

    def get_k_num(command):
        subed_arr = list()
        i = command[0]
        j = command[1]
        k = command[2]

        for index in range(i-1, j):
            subed_arr.append(array[index])

        subed_arr.sort()
        return subed_arr[k - 1]

    for command in commands:
        num = get_k_num(command=command)
        answer.append(num)

    return answer


result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(result)
