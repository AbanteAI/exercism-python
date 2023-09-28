import re

def answer(question):
    # Iteration 0 - Numbers
    if re.match(r"What is \d+\?", question):
        return int(question.split()[2])

    # Iteration 1 - Addition
    if "plus" in question:
        numbers = re.findall(r"\d+", question)
        return sum(map(int, numbers))

    # Iteration 2 - Subtraction, Multiplication, and Division
    if "minus" in question:
        numbers = re.findall(r"\d+", question)
        return int(numbers[0]) - int(numbers[1])
    if "multiplied by" in question:
        numbers = re.findall(r"\d+", question)
        return int(numbers[0]) * int(numbers[1])
    if "divided by" in question:
        numbers = re.findall(r"\d+", question)
        return int(numbers[0]) // int(numbers[1])

    # Iteration 3 - Multiple Operations
    if "plus" in question or "minus" in question or "multiplied by" in question or "divided by" in question:
        parts = re.split(r"(plus|minus|multiplied by|divided by)", question)
        result = int(parts[0].split()[2])
        for i in range(1, len(parts), 2):
            operator = parts[i].strip()
            number = int(parts[i + 1].strip())
            if operator == "plus":
                result += number
            elif operator == "minus":
                result -= number
            elif operator == "multiplied by":
                result *= number
            elif operator == "divided by":
                result //= number
        return result

    # Iteration 4 - Errors
    if re.match(r"What is \d+ \w+ \d+\?", question):
        raise ValueError("unsupported operation")
    if not re.match(r"What is \d+.*\d+\?", question):
        raise ValueError("non-math question")
    raise ValueError("syntax error")
