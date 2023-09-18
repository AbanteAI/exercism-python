class StackUnderflowError(Exception):
    pass


def add(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b + a)

def subtract(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)

def multiply(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b * a)

def divide(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b // a)

def dup(stack):
    stack.append(stack[-1])

def drop(stack):
    stack.pop()

def swap(stack):
    stack[-1], stack[-2] = stack[-2], stack[-1]

def over(stack):
    stack.append(stack[-2])

def parse_definition(input_data):
    definition_end = input_data.index(";")
    word_name = input_data[0]
    definition = input_data[1:definition_end]
    return word_name.lower(), definition, definition_end + 1

def evaluate(input_data: str):
    stack = []
    definitions = {}

    words = input_data.split()
    i = 0
    while i < len(words):
        word = words[i].lower()
        if word == ":":
            word_name, definition, offset = parse_definition(words[i + 1:])
            definitions[word_name] = definition
            i += offset
        elif word in definitions:
            words[i:i + 1] = definitions[word]
        elif word.isdigit() or (word[0] == "-" and word[1:].isdigit()):
            stack.append(int(word))
        elif word == "+":
            add(stack)
        elif word == "-":
            subtract(stack)
        elif word == "*":
            multiply(stack)
        elif word == "/":
            divide(stack)
        elif word == "dup":
            dup(stack)
        elif word == "drop":
            drop(stack)
        elif word == "swap":
            swap(stack)
        elif word == "over":
            over(stack)
        else:
            raise ValueError("Unknown word")
        i += 1

    return stack
