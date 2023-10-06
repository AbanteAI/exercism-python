def cipher_text(plain_text):
    normalized_text = "".join(char.lower() for char in plain_text if char.isalnum())
    size = len(normalized_text)
    rows = int(size ** 0.5)
    columns = rows + 1 if rows * rows < size else rows
    encoded_text = ""
    padding = rows * columns - size

    for col in range(columns):
        for row in range(rows):
            index = col + row * columns
            if index < size:
                encoded_text += normalized_text[index]
            else:
                encoded_text += " "
        if col >= columns - padding:
            encoded_text += " "

    return " ".join(encoded_text[i:i + columns] for i in range(0, len(encoded_text), columns))
