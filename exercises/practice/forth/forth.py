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
    
    def parse_number(token):
        try:
            return int(token)
        except ValueError:
            return None
    
    def parse_word_definition(tokens):
        if not tokens:
            return None
        if tokens[0].startswith(':'):
            name = tokens.pop(0)[1:].upper()
            definition = []
            while tokens and not tokens[0].startswith(';'):
                definition.append(tokens.pop(0))
            if tokens:
                tokens.pop(0)  # Remove ';'
            return name, definition
        return None
    
    for line in input_data:
        tokens = line.split()
        while tokens:
            word_def = parse_word_definition(tokens)
            if word_def:
                name, definition = word_def
                words[name.upper()] = definition
                continue
            
            token = tokens.pop(0).upper()
            number = parse_number(token)
            if number is not None:
                stack.append(number)
            elif token in words:
                tokens = words[token] + tokens
            elif token == "DUP":
                if not stack:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])
            elif token == "DROP":
                if not stack:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()
            elif token == "SWAP":
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack[-1], stack[-2] = stack[-2], stack[-1]
            elif token == "OVER":
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])
            elif token == "+":
                apply_operator(lambda a, b: a + b)
            elif token == "-":
                apply_operator(lambda a, b: a - b)
            elif token == "*":
                apply_operator(lambda a, b: a * b)
            elif token == "/":
                apply_operator(lambda a, b: a // b)
            else:
                raise ValueError("undefined operation")
    
    return stack