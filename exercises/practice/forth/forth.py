import re
class StackUnderflowError(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise StackUnderflowError("Stack is empty")
        return self.stack.pop()

    def top(self):
        if not self.stack:
            raise StackUnderflowError("Stack is empty")
        return self.stack[-1]

    def dup(self):
        self.push(self.top())

    def drop(self):
        self.pop()

    def swap(self):
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)

    def over(self):
        a = self.pop()
        b = self.top()
        self.push(a)
        self.push(b)
def evaluate(input_data):
    stack = Stack()
    words = {}

    def parse_word_definition(word_definition):
        name, definition = word_definition.split(" ", 1)
        return name.lower(), definition.strip()

    def parse_number(word):
        try:
            return int(word)
        except ValueError:
            return None

    def execute_word(word):
        if word in words:
            execute(words[word])
        elif word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
            stack.push(int(word))
        else:
            raise ValueError(f"Unknown word {word}")

    def execute(definition):
        for word in definition.split():
            execute_word(word.lower())

    for line in input_data.splitlines():
        if line.startswith(":"):
            name, definition = parse_word_definition(line[1:].strip())
            words[name] = definition
        else:
            execute(line)

    return stack.stack
