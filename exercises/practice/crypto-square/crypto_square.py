import re

def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = re.sub(r'[^a-z0-9]', '', plain_text.lower())

    # Normalize the input text
    normalized_text = re.sub(r'[^a-z0-9]', '', plain_text.lower())

    # Determine the size of the rectangle
    length = len(normalized_text)
    c = int(length**0.5)
    r = c if c * (c - 1) < length else c - 1

    # Adjust the number of columns if necessary
    if c * r < length:
        r += 1

    # Create the rectangle
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]

    # Pad the last row if it is short
    if len(rectangle[-1]) < c:
        rectangle[-1] += ' ' * (c - len(rectangle[-1]))

    # Read the rectangle column by column to get the encoded message
    encoded_message = ''
    for col in range(c):
        for row in rectangle:
            if col < len(row):
                encoded_message += row[col]
        if col < c - 1:
            encoded_message += ' '

    return encoded_message
