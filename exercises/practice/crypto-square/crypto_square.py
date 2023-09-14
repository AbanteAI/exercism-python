def cipher_text(plain_text):
    # Remove non-alphanumeric characters and convert to lowercase
    plain_text = ''.join(char.lower() for char in plain_text if char.isalnum())

    # Calculate the dimensions of the rectangle
    c = int(len(plain_text) ** 0.5)
    r = c if c * c == len(plain_text) else c + 1

    # Create the encrypted text
    encrypted_text = []
    for i in range(r):
        row = plain_text[i::r]
        if i == r - 1:
            row += ' ' * (r - len(row) - (len(plain_text) % r))
        else:
            row += ' ' * (r - len(row))
        encrypted_text.append(row)

    return ' '.join(encrypted_text)