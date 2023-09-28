import re
import math

def cipher_text(plain_text):
    # Step 1: Normalize the input text
    normalized_text = re.sub(r'\W+', '', plain_text).lower()

    # Step 2: Determine the number of rows and columns for the rectangle
    length = len(normalized_text)
    c = int(math.ceil(math.sqrt(length)))
    r = int(math.floor(math.sqrt(length)))
    if r * c < length:
        r += 1

    # Step 3: Organize the normalized text into a rectangle
    rectangle = [normalized_text[i:i+c] for i in range(0, length, c)]
    rectangle[-1] = rectangle[-1].ljust(c)
    # Step 4: Read the encoded message from the rectangle
    encoded_message = []
    for i in range(c):
        for row in rectangle:
            encoded_message.append(row[i])

        # Step 5: Output the encoded text in chunks, separated by spaces
        if i < c - 1:
            encoded_message.append(' ')