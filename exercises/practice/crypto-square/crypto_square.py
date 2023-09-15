def cipher_text(plain_text):
    # Normalize the input by removing spaces and punctuation and converting to lowercase
    normalized_text = "".join(char.lower() for char in plain_text if char.isalpha())

    # Determine the number of rows and columns for the rectangle
    length = len(normalized_text)
    rows = int(length ** 0.5)
    columns = rows if rows * rows >= length else rows + 1

    # Create the rectangle by breaking the normalized text into rows
    rectangle = [normalized_text[i:i+columns] for i in range(0, length, columns)]

    # Transpose the rectangle to read down the columns
    transposed_rectangle = ["".join(row[i] for row in rectangle) for i in range(columns)]

    # Add trailing spaces to the last row if necessary
    last_row_length = len(rectangle[-1]) if len(rectangle[-1]) == columns else columns
    transposed_rectangle[-1] += " " * (columns - last_row_length)

    # Join the transposed rectangle with spaces between chunks
    encoded_text = " ".join(transposed_rectangle)

    return encoded_text
