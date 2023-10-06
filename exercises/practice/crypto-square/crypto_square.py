def cipher_text(plain_text):
def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = ''.join(c.lower() for c in plain_text if c.isalnum())

    # Calculate the number of rows and columns for the rectangle
    length = len(normalized_text)
    columns = int(length ** 0.5) + (1 if length ** 0.5 % 1 > 0 else 0)
    rows = columns if columns * (columns - 1) < length else columns - 1

    # Organize the text into a rectangle
    rectangle = [normalized_text[i:i + columns] for i in range(0, length, columns)]

    # Encode the message by reading down the columns
    encoded_text = [''.join([row[i] if i < len(row) else ' ' for row in rectangle]) for i in range(columns)]

    # Output the encoded text in chunks separated by spaces
    return ' '.join(encoded_text)
