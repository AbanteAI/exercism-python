def is_paired(input_string):
    stack = []
    opening_brackets = ["[", "{", "("]
    closing_brackets = ["]", "}", ")"]

    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            if closing_brackets.index(char) != opening_brackets.index(stack.pop()):
                return False

    return len(stack) == 0
