class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    user_defined_words = {}
    tokens = iter(input_data.split())

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif token in user_defined_words:
            stack.extend(evaluate(user_defined_words[token]))
        elif token == "DUP":
            try:
                stack.append(stack[-1])
            except IndexError:
                raise StackUnderflowError("Not enough elements in the stack for this operation")
        elif token == "SWAP":
            try:
                stack[-1], stack[-2] = stack[-2], stack[-1]
            except IndexError:
                raise StackUnderflowError("Not enough elements in the stack for this operation")
        elif token == "OVER":
            try:
                stack.append(stack[-2])
            except IndexError:
                raise StackUnderflowError("Not enough elements in the stack for this operation")
        elif token == ":":
            word_name = next(tokens)
            if word_name.lstrip('-').isdigit():
                raise ValueError("Cannot redefine numbers")
            word_definition = []
            while (definition_token := next(tokens)) != ";":
                word_definition.append(definition_token)
            user_defined_words[word_name] = " ".join(word_definition)
        else:
            raise ValueError(f"Unknown token: {token}")

    return stack
