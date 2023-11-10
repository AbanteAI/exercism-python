def is_paired(input_string):
    # Define pairs of brackets
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is an opening bracket, push to stack
        if char in brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in brackets.values():
            # If stack is empty or doesn't match the corresponding opening bracket
            if not stack or brackets[stack.pop()] != char:
                return False

    # If stack is empty, all brackets are paired correctly
    return not stack