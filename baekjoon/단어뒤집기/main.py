
n = int(input())


def reverse(input_value: str) -> str:
    stack = []
    for word in input_value.split(" "):
        stack.append(word[::-1])
    return " ".join(stack)


ans = []

for _ in range(n):
    input_value = input()
    ans.append(reverse(input_value))

for a in ans:
    print(a)
