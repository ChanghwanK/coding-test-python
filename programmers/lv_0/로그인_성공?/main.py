# def solution(id_pw, db):
#     # ["meosseugi", "1234"]
#     # [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
#     # answer = "fail"
#     id: str = id_pw[0]
#     pw: str = id_pw[1]

#     for info in db:
#         # id가 일치
#         if info[0] == id:
#             # pw가 일치하는지
#             if info[1] == pw:
#                 answer = "login"
#             else:
#                 answer = "wrong pw"
#                 break
#         else:
#             answer = "fail"

#     return answer

def solution(id_pw, db):
    print("호출")
    # id: str = id_pw[0]
    # pw: str = id_pw[1]

    for a, b, c in db:  # 파이썬은 2차원 배열일 경우 2차원 배열의 인덱스에 한 번에 접근할 수 있음
        # id가 일치
        print(a)
        print(b)
        print(c)

    # return answer


solution(["meosseugi", "1234"], [["rardss", "123", "12345"],
         ["yyoom", "1234", "12345"], ["meosseugi", "1234", "12345"]])
