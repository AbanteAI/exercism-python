class StackUnderflowError(Exception):
    pass


import re

class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    stack = []
    words = {}

    def push(value):
        stack.append(value)

    def pop():
        if len(stack) < 1:
            raise StackUnderflowError("Not enough items on the stack")
        return stack.pop()

    def execute_word(word):
        if word in words:
            for w in words[word]:
                execute_word(w)
        elif word.isdigit():
            push(int(word))
        elif re.match(r"^[-+*/]$", word):
            b = pop()
            a = pop()
            if word == '+':
                push(a + b)
            elif word == '-':
                push(a - b)
            elif word == '*':
                push(a * b)
            elif word == '/':
                push(a // b)
        else:
            raise ValueError(f"Unknown word: {word}")

    def define_word(name, definition):
        words[name] = definition

    for input_line in input_data:
        input_words = input_line.replace('\n', ' ').split()
        i = 0
        while i < len(input_words):
            word = input_words[i].upper()

            if word == ":":
                name = input_words[i + 1]
                definition = []
                i += 2
                while input_words[i] != ";":
                    definition.append(input_words[i])
                    i += 1
                define_word(name.upper(), definition)
            else:
                execute_word(word)
            i += 1

    return stack
