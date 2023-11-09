class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message="Insufficient number of items in stack"):
        self.message = message
        super().__init__(self.message)


def evaluate(input_data):
    stack = []
    definitions = {}

    def get_value():
        if not stack:
            raise StackUnderflowError("Cannot perform operation because the stack is empty")
        return stack.pop()

    def perform_operation(operator):
        b = get_value()
        a = get_value()
        if operator == '+':
            stack.append(a + b)
        elif operator == '-':
            stack.append(a - b)
        elif operator == '*':
            stack.append(a * b)
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            stack.append(a // b)

    for item in ' '.join(input_data).upper().split():
        if item.isdigit():
            stack.append(int(item))
        elif item in definitions:
            for word in definitions[item].split():
                if word.isdigit():
                    stack.append(int(word))
                else:
                    perform_operation(word)
        elif item in '+-*/':
            perform_operation(item)
        elif item == 'DUP':
            if not stack:
                raise StackUnderflowError("Cannot duplicate because the stack is empty")
            stack.append(stack[-1])
        elif item == 'DROP':
            get_value()
        elif item == 'SWAP':
            b = get_value()
            a = get_value()
            stack.extend([b, a])
        elif item == 'OVER':
            if len(stack) < 2:
                raise StackUnderflowError("Cannot perform 'over' because there are not enough values in the stack")
            stack.append(stack[-2])
        elif item == ':':
            name = next(input_data).upper()
            definition = []
            while True:
                word = next(input_data).upper()
                if word == ';':
                    break
                definition.append(word)
            definitions[name] = ' '.join(definition)
        else:
            raise ValueError(f"Unknown command or value: {item}")

    return stack
