import re

def answer(question):
    # Iteration 0 - Numbers
    if re.match(r"What is \d+\?", question):
        return int(question.split()[2])

    # Iteration 1 - Addition
    if re.match(r"What is \d+ plus \d+\?", question):
        numbers = re.findall(r"\d+", question)
        return int(numbers[0]) + int(numbers[1])

    # Iteration 2 - Subtraction, Multiplication, and Division
    if re.match(r"What is \d+ (minus|multiplied by|divided by) \d+\?", question):
        numbers = re.findall(r"\d+", question)
        if "minus" in question:
            return int(numbers[0]) - int(numbers[1])
        elif "multiplied by" in question:
            return int(numbers[0]) * int(numbers[1])
        elif "divided by" in question:
            return int(numbers[0]) / int(numbers[1])

    # Iteration 3 - Multiple Operations
    if re.match(r"What is \d+ (plus|minus|multiplied by|divided by) \d+ (plus|minus|multiplied by|divided by) \d+\?", question):
        numbers = re.findall(r"\d+", question)
        operations = re.findall(r"(plus|minus|multiplied by|divided by)", question)
        result = int(numbers[0])
        for i in range(1, len(numbers)):
            if operations[i-1] == "plus":
                result += int(numbers[i])
            elif operations[i-1] == "minus":
                result -= int(numbers[i])
            elif operations[i-1] == "multiplied by":
                result *= int(numbers[i])
            elif operations[i-1] == "divided by":
                result /= int(numbers[i])
        return result

    # Iteration 4 - Errors
    if re.match(r"What is \d+ (cubed|plus plus \d+)\?", question):
        raise ValueError("Unsupported operation")
    if re.match(r"(Who|What) is", question):
        raise ValueError("Non-math question")
    if re.match(r"What is \d+ (plus|minus|multiplied by|divided by) \d+ (plus|minus|multiplied by|divided by) \d+ (plus|minus|multiplied by|divided by)", question):
        raise ValueError("Invalid syntax")
