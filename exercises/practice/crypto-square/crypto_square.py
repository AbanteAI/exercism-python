def cipher_text(plain_text):
    pass
def normalize_text(text):
    normalized = "".join(c.lower() for c in text if c.isalnum())
    return normalized

def square_dimensions(length):
    cols = int(length ** 0.5)
    rows = cols if cols * cols >= length else cols + 1
    return rows, cols

def cipher_text(plain_text):
    normalized = normalize_text(plain_text)
    if not normalized:
        return ""

    rows, cols = square_dimensions(len(normalized))
    result = []

    for col in range(cols):
        row_string = ""
        for row in range(rows):
            index = col + row * cols
            if index < len(normalized):
                row_string += normalized[index]
        result.append(row_string)

    return " ".join(result)
