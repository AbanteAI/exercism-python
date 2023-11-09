class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message="Insufficient number of items in stack"):
        self.message = message
        super().__init__(self.message)


def evaluate(input_data):
    # Helper functions
    def perform_arithmetic_operation(operation, stack):
        if len(stack) < 2:
            raise StackUnderflowError()
        b, a = stack.pop(), stack.pop()
        if operation == '+':
            stack.append(a + b)
        elif operation == '-':
            stack.append(a - b)
        elif operation == '*':
            stack.append(a * b)
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)

    def perform_stack_manipulation(operation, stack):
        if operation == 'DUP':
            if not stack:
                raise StackUnderflowError()
            stack.append(stack[-1])
        elif operation == 'DROP':
            if not stack:
                raise StackUnderflowError()
            stack.pop()
        elif operation == 'SWAP':
            if len(stack) < 2:
                raise StackUnderflowError()
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif operation == 'OVER':
            if len(stack) < 2:
                raise StackUnderflowError()
            stack.append(stack[-2])

    def define_new_word(definition, word_definitions):
        if definition[0] != ':' or definition[-1] != ';':
            raise ValueError("Invalid word definition syntax")
        parts = definition[1:-1].split()
        name = parts[0].upper()
        if name.isdigit():
            raise ValueError("Word name cannot be a number")
        body = parts[1:]
        word_definitions[name] = body

    # Main evaluation function
    stack = []
    word_definitions = {}
    for line in input_data:
        words = line.split()
        for word in words:
            word = word.upper()
            if word.isdigit():
                stack.append(int(word))
            elif word in word_definitions:
                evaluate(word_definitions[word])
            elif word in ['+', '-', '*', '/']:
                perform_arithmetic_operation(word, stack)
            elif word in ['DUP', 'DROP', 'SWAP', 'OVER']:
                perform_stack_manipulation(word, stack)
            elif word.startswith(':') and word.endswith(';'):
                define_new_word(words, word_definitions)
                break  # Exit the loop after defining a new word
            else:
                raise ValueError("undefined operation")
    return stack
