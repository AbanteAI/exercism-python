class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message="Insufficient number of items in stack"):
        self.message = message
        super().__init__(self.message)


def evaluate(input_data_list):
    # Define the stack and a dictionary for custom words
    stack = []
    definitions = {}

    # Helper function to ensure there are enough items on the stack
    def require_stack_size(size):
        if len(stack) < size:
            raise StackUnderflowError()

    # Helper function to parse and execute a word
    def execute_word(word):
        if word.isdigit():
            stack.append(int(word))
        elif word == '+':
            require_stack_size(2)
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif word == '-':
            require_stack_size(2)
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif word == '*':
            require_stack_size(2)
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif word == '/':
            require_stack_size(2)
            b, a = stack.pop(), stack.pop()
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)
        elif word.upper() == 'DUP':
            require_stack_size(1)
            stack.append(stack[-1])
        elif word.upper() == 'DROP':
            require_stack_size(1)
            stack.pop()
        elif word.upper() == 'SWAP':
            require_stack_size(2)
            stack[-2], stack[-1] = stack[-1], stack[-2]
        elif word.upper() == 'OVER':
            require_stack_size(2)
            stack.append(stack[-2])
        elif word.upper() in definitions:
            for def_word in definitions[word.upper()].split():
                execute_word(def_word)
        else:
            raise ValueError(f"undefined operation: {word}")

    # Concatenate the list of input strings into a single space-separated string
    input_data = ' '.join(input_data_list)

    # Split the input data into words and process each one
    words = input_data.split()
    index = 0
    while index < len(words):
        word = words[index]
        if word == ':':
            index += 1
            if index >= len(words):
                raise ValueError("incomplete definition")
            name = words[index].upper()
            if name.isdigit():
                raise ValueError("invalid definition name")
            index += 1
            definition = []
            while index < len(words) and words[index] != ';':
                definition.append(words[index])
                index += 1
            if index >= len(words) or words[index] != ';':
                raise ValueError("missing ; to end definition")
            definitions[name] = ' '.join(definition)
        else:
            execute_word(word)
        index += 1

    return stack
    index = 0
    while index < len(words):
        word = words[index]
        if word == ':':
            index += 1
            if index >= len(words):
                raise ValueError("incomplete definition")
            name = words[index].upper()
            if name.isdigit():
                raise ValueError("invalid definition name")
            index += 1
            definition = []
            while index < len(words) and words[index] != ';':
                definition.append(words[index])
                index += 1
            if index >= len(words) or words[index] != ';':
                raise ValueError("missing ; to end definition")
            definitions[name] = ' '.join(definition)
        else:
            execute_word(word)
        index += 1

    return stack
