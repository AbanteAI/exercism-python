def answer(question):
    pass

def tokenize(question):
    question = question.strip("?").replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/")
    tokens = [token.strip() for token in question.split() if token.strip() not in ["What", "is"]]
    return tokens

def evaluate(tokens):
    try:
        result = int(tokens[0])
    except (ValueError, IndexError):
        raise ValueError("syntax error")

    for i in range(1, len(tokens), 2):
        if tokens[i] == "+":
            try:
                result += int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        elif tokens[i] == "-":
            try:
                result -= int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        elif tokens[i] == "*":
            try:
                result *= int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        elif tokens[i] == "/":
            try:
                result //= int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")
    return result
        elif tokens[i] == "-":
            try:
                result -= int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        elif tokens[i] == "*":
            try:
                result *= int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        elif tokens[i] == "/":
            try:
                result //= int(tokens[i + 1])
            except ValueError:
                raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")
    return result

def answer(question):
    tokens = tokenize(question)
    return evaluate(tokens)