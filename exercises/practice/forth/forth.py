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

    def arithmetic_operation(operation):
        if len(stack) < 2:
            raise StackUnderflowError("Stack underflow")
        b = pop()
        a = pop()
        if operation == '+':
            push(a + b)
        elif operation == '-':
            push(a - b)
        elif operation == '*':
            push(a * b)
        elif operation == '/':
            push(a // b)

    def stack_manipulation_operation(operation):
        if operation == 'DUP':
            if len(stack) < 1:
                raise StackUnderflowError("Stack underflow")
            push(stack[-1])
        elif operation == 'DROP':
            if len(stack) < 1:
                raise StackUnderflowError("Stack underflow")
            pop()
        elif operation == 'SWAP':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            b = pop()
            a = pop()
            push(b)
            push(a)
        elif operation == 'OVER':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            b = pop()
            a = pop()
            push(a)
            push(b)
            push(a)

    def define_word(word_name, definition):
        words[word_name] = definition

    def execute_word(word_name):
        if word_name in words:
            definition = words[word_name]
            evaluate(definition)
        else:
            raise ValueError(f"Undefined word: {word_name}")

    def parse_input(input_data):
        words_list = input_data.split()
        for word in words_list:
            if word.isdigit():
                push(int(word))
            else:
                word = word.upper()
                if word in ['+', '-', '*', '/']:
                    arithmetic_operation(word)
                elif word in ['DUP', 'DROP', 'SWAP', 'OVER']:
                    stack_manipulation_operation(word)
                elif word == ':':
                    word_name = words_list.pop(0)
                    definition = []
                    while words_list[0] != ';':
                        definition.append(words_list.pop(0))
                    words_list.pop(0)  # Remove the ';'
                    define_word(word_name, definition)
                else:
                    execute_word(word)

    parse_input(input_data)
    return stack[-1]
    pass
