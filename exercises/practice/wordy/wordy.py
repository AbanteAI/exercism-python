import re

def answer(question):
    question = question.strip("?").replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/")
    tokens = re.split(r'\s+', question)

    if len(tokens) < 3:
        raise ValueError("syntax error")

    if not tokens[0].lower() == "what" or not tokens[1].lower() == "is":
        raise ValueError("unknown operation")

    index = 2
    result = 0
    current_operation = None

    while index < len(tokens):
        token = tokens[index]

        if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
            number = int(token)

            if current_operation is None:
                if index != 2:
                    raise ValueError("syntax error")
                result = number
            elif current_operation == "+":
                result += number
            elif current_operation == "-":
                result -= number
            elif current_operation == "*":
                result *= number
            elif current_operation == "/":
                result //= number
            else:
                raise ValueError("unknown operation")

            current_operation = None
        elif token in ["+", "-", "*", "/"]:
            if current_operation is not None:
                raise ValueError("syntax error")
            current_operation = token
        else:
            raise ValueError("unknown operation")

        index += 1

    if current_operation is not None:
        raise ValueError("syntax error")

    return result