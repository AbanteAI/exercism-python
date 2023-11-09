import math

def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = ''.join(char for char in plain_text.lower() if char.isalnum())

    # Calculate the number of columns and rows for the rectangle
    length = len(normalized_text)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)

    # Ensure that c >= r and c - r <= 1
    if c < r:
        c, r = r, c
    elif c - r > 1:
        r += 1

    # Create the rectangle by breaking the normalized text into rows
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]

    # Pad the last row with spaces if necessary
    rectangle[-1] = rectangle[-1].ljust(c)

    # Encode the message by reading down the columns from left to right
    encoded_chunks = [''.join(row[i] for row in rectangle if i < len(row)) for i in range(c)]

    # Pad the last n chunks with a single trailing space if necessary
    short = c * r - length
    if short:
        encoded_chunks[-short:] = [chunk + ' ' for chunk in encoded_chunks[-short:]]

    # Join the chunks with spaces and return the encoded message
    return ' '.join(encoded_chunks)
