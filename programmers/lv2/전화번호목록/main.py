def solution(phone_book):
    # 폰북 dict 만들기
    # phone_book arr 돌면서 key 검사
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer


print(solution(["119", "97674223", "1195524421"]))
