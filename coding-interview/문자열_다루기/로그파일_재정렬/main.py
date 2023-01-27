from typing import List


def re_order_log_files(logs: List[str]) -> List[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    print(letters)
    print(digits)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits


print(re_order_log_files(
    [
        "dig1 8 1 5 1",
        "let1 art cat",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"
    ]
))
