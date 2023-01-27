def reverse_string(word: str) -> str:
    s = list()
    for char in word:
        s.append(char)

    s = "".join(s)
    return s[::-1]


print(reverse_string("hello"))
