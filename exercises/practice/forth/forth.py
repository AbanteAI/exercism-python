class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = []
    definitions = {}

    def get_value(word):
        try:
            return int(word)
        except ValueError:
            return word

    def apply_operation(op):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        b, a = stack.pop(), stack.pop()
        if op == '+':
            stack.append(a + b)
        elif op == '-':
            stack.append(a - b)
        elif op == '*':
            stack.append(a * b)
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)
        else:
            raise ValueError("undefined operation")

    for item in input_data:
        words = item.lower().split()
        index = 0
        while index < len(words):
            word = words[index]
            if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                stack.append(int(word))
            elif word in definitions:
                words.extend(definitions[word].split())
            elif word == ':':
                index += 1
                definition_name = words[index].lower()
                index += 1
                definition = []
                while words[index] != ';':
                    definition.append(words[index])
                    index += 1
                definitions[definition_name] = ' '.join(definition)
            elif word in ['+', '-', '*', '/']:
                apply_operation(word)
            elif word == 'dup':
                if not stack:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])
            elif word == 'drop':
                if not stack:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()
            elif word == 'swap':
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack[-2], stack[-1] = stack[-1], stack[-2]
            elif word == 'over':
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])
            else:
                raise ValueError(f"undefined operation {word}")
            index += 1
    return stack
