class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message="Insufficient number of items in stack"):
        self.message = message
        super().__init__(self.message)


def evaluate(input_data):
    # Initialize the stack and the word definitions
    stack = []
    definitions = {}

    # Helper function to check stack length
    def require_stack_length(length):
        if len(stack) < length:
            raise StackUnderflowError()

    # Helper function to define new words
    def define_word(word, definition):
        definitions[word.upper()] = definition

    # Helper function to process a single command
    def process_command(command):
        tokens = command.upper().split()
        for token in tokens:
            if token.isdigit():  # Numbers get pushed onto the stack
                stack.append(int(token))
            elif token in definitions:  # Defined words are evaluated
                process_command(definitions[token])
            elif token == '+':
                require_stack_length(2)
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                require_stack_length(2)
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                require_stack_length(2)
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                require_stack_length(2)
                b, a = stack.pop(), stack.pop()
                if b == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(a // b)
            elif token == 'DUP':
                require_stack_length(1)
                stack.append(stack[-1])
            elif token == 'DROP':
                require_stack_length(1)
                stack.pop()
            elif token == 'SWAP':
                require_stack_length(2)
                stack[-2], stack[-1] = stack[-1], stack[-2]
            elif token == 'OVER':
                require_stack_length(2)
                stack.append(stack[-2])
            elif token == ':':  # Start of word definition
                if not tokens:
                    raise ValueError("incomplete definition")
                name = tokens.pop(0)
                if not name.isalpha():
                    raise ValueError("illegal operation")
                definition = []
                while tokens and tokens[0] != ';':
                    definition.append(tokens.pop(0))
                if not tokens or tokens[0] != ';':
                    raise ValueError("incomplete definition")
                tokens.pop(0)  # Remove the closing ';'
                define_word(name, ' '.join(definition))
            else:
                raise ValueError("undefined operation")

    # Process each command in the input list
    for command in input_data:
        process_command(command)

    # Return the stack
    return stack
