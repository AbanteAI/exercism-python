def is_paired(input_string):
    bracket_map = {')': '(', '}': '{', ']': '['}
    open_brackets = set(bracket_map.values())
    stack = []

    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack
