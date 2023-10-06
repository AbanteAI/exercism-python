class StackUnderflowError(Exception):
    pass


    stack = []
    words = {}

    def evaluate(input_data):
        tokens = input_data.split()
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token in words:
                evaluate(words[token])
            else:
                if token == '+':
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif token == '-':
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                elif token == '*':
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                elif token == '/':
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a // b)
                elif token == 'DUP':
                    if len(stack) < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    stack.append(stack[-1])
                elif token == 'DROP':
                    if len(stack) < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    stack.pop()
                elif token == 'SWAP':
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(b)
                    stack.append(a)
                elif token == 'OVER':
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a)
                    stack.append(b)
                else:
                    raise ValueError("Undefined operation")

    def define_word(word_name, definition):
        words[word_name] = definition

