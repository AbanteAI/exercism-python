import re

def answer(question):
import re

def answer(question):
    # Remove the question mark and 'What is' from the question
    question = question.replace('?', '').strip()

    # Check if the question is a non-math question
    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    # Remove 'What is' from the question
    question = question.replace('What is ', '', 1)

    # Define the operation functions
    operations = {
        'plus': lambda x, y: x + y,
        'minus': lambda x, y: x - y,
        'multiplied by': lambda x, y: x * y,
        'divided by': lambda x, y: x // y
    }

    # Find all numbers in the question
    numbers = list(map(int, re.findall(r'-?\d+', question)))

    # Find all operations in the question
    ops = re.findall(r'plus|minus|multiplied by|divided by', question)

    # If there are no operations, return the number if there's exactly one number
    if not ops:
        if len(numbers) == 1:
            return numbers[0]
        else:
            raise ValueError("syntax error")

    # Check for invalid syntax
    if len(numbers) != len(ops) + 1:
        raise ValueError("syntax error")

    # Evaluate the expression from left-to-right
    result = numbers[0]
    for i, op in enumerate(ops):
        if op not in operations:
            raise ValueError("unknown operation")
        result = operations[op](result, numbers[i + 1])

    return result