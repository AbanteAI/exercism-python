def cipher_text(plain_text):
    # Step 1: Normalize the input text
    normalized_text = ''.join(c.lower() for c in plain_text if c.isalnum())

    # Step 2: Calculate the number of rows and columns for the rectangle
    length = len(normalized_text)
    if length == 0:
        return ""
    columns = int(length**0.5) + (1 if length**0.5 % 1 > 0 else 0)
    rows = length // columns + (1 if length % columns > 0 else 0)

    # Step 3: Organize the normalized text into a rectangle
    rectangle = [normalized_text[i:i+columns] for i in range(0, length, columns)]

    # Step 4: Read down the columns, left to right, to create the encoded message
    encoded_message = ''.join(''.join(row[i] for row in rectangle if i < len(row)) for i in range(columns))

    # Step 5: Output the encoded message in chunks separated by spaces
    return ' '.join(encoded_message[i:i+rows].ljust(rows, ' ') for i in range(0, length, rows))