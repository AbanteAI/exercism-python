import math

def cipher_text(plain_text):
    if not plain_text:
        return ""

    normalized_text = ''.join(c.lower() for c in plain_text if c.isalnum())

    square_size = int(math.ceil(math.sqrt(len(normalized_text))))
    rows = [normalized_text[i:i + square_size] for i in range(0, len(normalized_text), square_size)]

    encrypted_text = []
    for i in range(square_size):
        encrypted_row = ''.join(row[i] if i < len(row) else ' ' for row in rows)
        encrypted_text.append(encrypted_row)

    return ' '.join(encrypted_text)