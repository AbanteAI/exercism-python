class StackUnderflowError(Exception):
    pass


def evaluate(input_list):
    stack = []
    input_data = " ".join(input_list)
    definitions = {}

    def apply_operation(operation):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        b, a = stack.pop(), stack.pop()
        if operation == "+":
            stack.append(a + b)
        elif operation == "-":
            stack.append(a - b)
        elif operation == "*":
            stack.append(a * b)
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)

    def apply_stack_manipulation(operation):
        if operation == "DUP":
            if not stack:
                raise StackUnderflowError("Empty stack")
            stack.append(stack[-1])
        elif operation == "DROP":
            if not stack:
                raise StackUnderflowError("Empty stack")
            stack.pop()
        elif operation == "SWAP":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif operation == "OVER":
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-2])

    def process_token(token):
        if token.isdigit():
            stack.append(int(token))
        elif token.upper() in {"+", "-", "*", "/"}:
            apply_operation(token.upper())
        elif token.upper() in {"DUP", "DROP", "SWAP", "OVER"}:
            apply_stack_manipulation(token.upper())
        elif token.upper() in definitions:
            for definition_token in definitions[token.upper()]:
                process_token(definition_token)
        else:
            raise ValueError(f"undefined operation: {token}")

    tokens = input_data.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == ":":
            i += 1
            word_name = tokens[i].upper()
            definition = []
            i += 1
            while tokens[i] != ";":
                definition.append(tokens[i])
                i += 1
            definitions[word_name] = definition
        else:
            process_token(token)
        i += 1

    return stack