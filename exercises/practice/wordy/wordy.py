import re
def answer(question):
    operations = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied by": lambda x, y: x * y,
        "divided by": lambda x, y: x // y,
    }

    question = question.replace("?", "")
    tokens = re.findall(r"(-?\d+|plus|minus|multiplied by|divided by)", question)

    if len(tokens) < 3 or not tokens[0].lstrip('-').isdigit():
        raise ValueError("syntax error")

    result = int(tokens[0])

    i = 1
    while i < len(tokens) - 1:
        operation = tokens[i]
        if operation.isdigit():
            raise ValueError("syntax error")

        if i + 1 >= len(tokens) or not tokens[i + 1].lstrip('-').isdigit():
            raise ValueError("syntax error")

        result = operations[operation](result, int(tokens[i + 1]))
        i += 2

    return result