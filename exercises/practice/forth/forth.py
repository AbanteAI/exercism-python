class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = Stack()
    words = input_data
    for word in words:
        if word.isdigit():
            stack.push(int(word))
        elif word == "+":
            stack.push(stack.pop() + stack.pop())
        elif word == "-":
            stack.push(-stack.pop() + stack.pop())
        elif word == "*":
            stack.push(stack.pop() * stack.pop())
        elif word == "/":
            divisor = stack.pop()
            stack.push(stack.pop() // divisor)
        elif word == "DUP":
            stack.push(stack.peek())
        elif word == "DROP":
            stack.pop()
        elif word == "SWAP":
            a = stack.pop()
            b = stack.pop()
            stack.push(a)
            stack.push(b)
        elif word == "OVER":
            a = stack.pop()
            b = stack.pop()
            stack.push(b)
            stack.push(a)
            stack.push(b)
        else:
            raise ValueError(f"Undefined operation: {word}")
    return stack.items


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Insufficient number of items in stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Insufficient number of items in stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
