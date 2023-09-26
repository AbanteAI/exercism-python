def is_paired(input_string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack