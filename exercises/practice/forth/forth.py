class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    words = {}

    def apply_operator(operator):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        b = stack.pop()
        a = stack.pop()
        stack.append(operator(a, b))

    def define_word(name, definition):
        words[name.lower()] = definition

    def execute_word(name):
        if name.lower() in words:
            for token in words[name.lower()]:
                process_token(token)
        elif name.lower() in operations:
            operations[name.lower()]()
        else:
            raise ValueError("undefined operation")

    def process_token(token):
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        else:
            execute_word(token)

    operations = {
        '+': lambda: apply_operator(lambda a, b: a + b),
        '-': lambda: apply_operator(lambda a, b: a - b),
        '*': lambda: apply_operator(lambda a, b: a * b),
        '/': lambda: apply_operator(lambda a, b: a // b),
        'dup': lambda: stack.append(stack[-1]),
        'drop': lambda: stack.pop(),
        'swap': lambda: stack[-1], stack[-2] = stack[-2], stack[-1],
        'over': lambda: stack.append(stack[-2]),
    }

    for line in input_data:
        tokens = line.split()
        if tokens[0].lower() == ':':
            define_word(tokens[1], tokens[2:-1])
        else:
            for token in tokens:
                process_token(token)

    return stack