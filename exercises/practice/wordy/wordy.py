def answer(question):
    pass
import re

def parse_question(question):
    question = question.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/")
    tokens = re.findall(r"[-+*/]|\d+", question)
    numbers = [int(num) for num in re.findall(r"-?\d+", question)]
    operations = [op for op in tokens if not op.isdigit() and op != '-']
    return numbers, operations

def answer(question):
    numbers, operations = parse_question(question)
    if not numbers:
        return None
    if len(operations) != len(numbers) - 1:
        raise ValueError("Invalid syntax")

    result = numbers[0]
    for i, op in enumerate(operations):
        if op == "+":
            result += numbers[i + 1]
        elif op == "-":
            result -= numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "/":
            result //= numbers[i + 1]

    return result
