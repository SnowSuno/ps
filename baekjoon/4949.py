mapping = {
    "(": ")",
    "[": "]",
}


def is_balanced(string):
    stack = []

    for char in string:
        if char in mapping:
            stack.append(char)
        elif char in mapping.values():
            if len(stack) == 0:
                return False
            if mapping[stack.pop()] != char:
                return False
    return len(stack) == 0


while True:
    input_str = input()

    if input_str == ".":
        break

    if is_balanced(input_str):
        print("yes")
    else:
        print("no")
