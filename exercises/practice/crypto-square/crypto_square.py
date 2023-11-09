import math

def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = ''.join(char for char in plain_text.lower() if char.isalnum())

    # Determine the number of columns and rows for the rectangle
    length = len(normalized_text)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)

    # Create the rectangle with the normalized text
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]

    # Pad the last few elements with spaces if they are short
    padding = c * r - length
    if padding:
        rectangle[-1] = rectangle[-1].ljust(len(rectangle[-1]) + padding)

    # Encode the message by reading down the columns
    encoded_message = []
    for col in range(c):
        column_chars = [row[col] if col < len(row) else ' ' for row in rectangle]
        encoded_message.append(''.join(column_chars))

    # Join the encoded message with spaces and return
    return ' '.join(encoded_message).rstrip()
