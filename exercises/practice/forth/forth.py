class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    words = {}

    def push(value):
        stack.append(value)

    def pop():
        if len(stack) == 0:
            raise StackUnderflowError("Stack underflow")
        return stack.pop()

    def add():
        a = pop()
        b = pop()
        push(a + b)

    def subtract():
        a = pop()
        b = pop()
        push(b - a)

    def multiply():
        a = pop()
        b = pop()
        push(a * b)

    def divide():
        a = pop()
        b = pop()
        push(b // a)

    def duplicate():
        a = pop()
        push(a)
        push(a)

    def drop():
        pop()

    def swap():
        a = pop()
        b = pop()
        push(a)
        push(b)

    def over():
        a = pop()
        b = pop()
        push(b)
        push(a)
        push(b)

    def define_word(word_name, definition):
        words[word_name] = definition

    for token in input_data.split():
        if token.isdigit():
            push(int(token))
        elif token in words:
            evaluate(words[token])
        elif token == "+":
            add()
        elif token == "-":
            subtract()
        elif token == "*":
            multiply()
        elif token == "/":
            divide()
        elif token == "DUP":
            duplicate()
        elif token == "DROP":
            drop()
        elif token == "SWAP":
            swap()
        elif token == "OVER":
            over()

    return stack[-1] if stack else None
