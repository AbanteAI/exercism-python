import re

import re

def answer(question):
    numbers = re.findall(r"-?\d+", question)
    operations = re.findall(r"plus|minus|multiplied by|divided by", question)
    if len(numbers) != len(operations) + 1:
        raise ValueError("Invalid syntax")

    result = int(numbers[0])
    for i in range(len(operations)):
        if operations[i] == "plus":
            result += int(numbers[i + 1])
        elif operations[i] == "minus":
            result -= int(numbers[i + 1])
        elif operations[i] == "multiplied by":
            result *= int(numbers[i + 1])
        elif operations[i] == "divided by":
            result /= int(numbers[i + 1])
    return result