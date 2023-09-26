def is_paired(input_string):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    return not stack
