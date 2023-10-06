class StackUnderflowError(Exception):
    pass


import re

class ForthEvaluator:
    def __init__(self):
        self.stack = []
        self.words = {}

    def evaluate(self, input_data):
        input_str = ' '.join(input_data)
        tokens = re.findall(r'\S+', input_str.lower())
        for token in tokens:
            self.process_token(token)
        return self.stack

    def process_token(self, token):
        if token.isdigit():
            self.stack.append(int(token))
        elif token in self.words:
            for word_token in self.words[token]:
                self.process_token(word_token)
        else:
            self.execute_operation(token)

    def execute_operation(self, operation):
        if operation == "+":
            self.add()
        elif operation == "-":
            self.subtract()
        elif operation == "*":
            self.multiply()
        elif operation == "/":
            self.divide()
        elif operation == "dup":
            self.dup()
        elif operation == "drop":
            self.drop()
        elif operation == "swap":
            self.swap()
        elif operation == "over":
            self.over()
        else:
            raise ValueError(f"Undefined operation: {operation}")

    def add(self):
        self.ensure_stack_size(2)
        self.stack.append(self.stack.pop() + self.stack.pop())

    def subtract(self):
        self.ensure_stack_size(2)
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def multiply(self):
        self.ensure_stack_size(2)
        self.stack.append(self.stack.pop() * self.stack.pop())

    def divide(self):
        self.ensure_stack_size(2)
        b = self.stack.pop()
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        a = self.stack.pop()
        self.stack.append(a // b)

    def dup(self):
        self.ensure_stack_size(1)
        self.stack.append(self.stack[-1])

    def drop(self):
        self.ensure_stack_size(1)
        self.stack.pop()

    def swap(self):
        self.ensure_stack_size(2)
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def over(self):
        self.ensure_stack_size(2)
        self.stack.append(self.stack[-2])

    def ensure_stack_size(self, size):
        if len(self.stack) < size:
            raise StackUnderflowError(f"Insufficient number of items in stack: {len(self.stack)}")

def evaluate(input_data):
    evaluator = ForthEvaluator()
    return evaluator.evaluate(input_data)