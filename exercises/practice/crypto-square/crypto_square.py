def cipher_text(plain_text):
    # Normalize the input text
    normalized_text = ''.join(filter(str.isalnum, plain_text)).lower()

    # Determine the size of the rectangle
    length = len(normalized_text)
    c = r = int(length**0.5)
    if c * r < length:
        c += 1
    if c * r < length:
        r += 1

    # Organize the text into the rectangle
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]

    # Pad the last few elements if necessary
    padding = c - len(rectangle[-1])
    for i in range(1, padding + 1):
        rectangle[-i] += ' '

    # Encode the message
    encoded_message = ''
    # Encode the message
    encoded_message = ''
    for i in range(c):
        for row in rectangle:
            if i < len(row):
                encoded_message += row[i]
        encoded_message += ' '
    return encoded_message.rstrip()

    return encoded_message.strip()