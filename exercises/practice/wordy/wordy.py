import re

def answer(question):
    question = question.replace("?", "")
    numbers = list(map(int, re.findall(r"-?\d+", question)))
    operations = re.findall(r"(?:plus|minus|multiplied by|divided by)", question)

    if len(numbers) != len(operations) + 1:
        raise ValueError("Invalid syntax")

    result = numbers[0]
    for i in range(len(operations)):
        if operations[i] == "plus":
            result += numbers[i + 1]
        elif operations[i] == "minus":
            result -= numbers[i + 1]
        elif operations[i] == "multiplied by":
            result *= numbers[i + 1]
        elif operations[i] == "divided by":
            result //= numbers[i + 1]

    return result
    def answer(question):
        question = question.replace("?", "")
        numbers = list(map(int, re.findall(r"-?\d+", question)))
        operations = re.findall(r"(?:plus|minus|multiplied by|divided by)", question)

        if len(numbers) != len(operations) + 1:
            raise ValueError("Invalid syntax")

        result = numbers[0]
        for i in range(len(operations)):
            if operations[i] == "plus":
                result += numbers[i + 1]
            elif operations[i] == "minus":
                result -= numbers[i + 1]
            elif operations[i] == "multiplied by":
                result *= numbers[i + 1]
            elif operations[i] == "divided by":
                result //= numbers[i + 1]

        return result
