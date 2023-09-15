import math

def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = ''.join(c.lower() for c in plain_text if c.isalnum())
    if not normalized_text:
        return ""

    # Determine the rectangle dimensions
    length = len(normalized_text)
    c = int(math.ceil(math.sqrt(length)))
    r = int(math.ceil(length / c))

    # Organize the normalized text into a rectangle
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]

    # Read down the columns and output the encoded text
    encoded_text = ' '.join(''.join(row[i] if i < len(row) else ' ' for row in rectangle) for i in range(c))
    return encoded_text