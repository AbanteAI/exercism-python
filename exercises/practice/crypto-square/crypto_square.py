import re
import math

def cipher_text(plain_text):
    # Normalize the input
    normalized_text = re.sub(r'[^a-z0-9]', '', plain_text.lower())
    
    # Calculate the number of columns and rows
    length = len(normalized_text)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)
    
    # Ensure the rectangle is as square as possible
    if c > r and c - r > 1:
        c -= 1
        r += 1
    
    # Create the rectangle
    rectangle = [normalized_text[i * c:(i + 1) * c].ljust(c, ' ') for i in range(r)]
    
    # Encode the message
    encoded_message = ''
    for i in range(c):
        for row in rectangle:
            encoded_message += row[i]
        if i < c - 1:
            encoded_message += ' '
    
    # Output the encoded text with proper padding
    return encoded_message.rstrip()
