def is_paired(input_string):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0