def is_paired(input_string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack