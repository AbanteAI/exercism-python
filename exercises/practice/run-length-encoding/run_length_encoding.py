import re

def decode(string):
    decoded = []
    pattern = re.compile(r'(\d*)(\D)')
    for count, char in pattern.findall(string):
        count = int(count) if count else 1
        decoded.append(char * count)
    return ''.join(decoded)


def encode(string):
    encoded = []
    current_char = ''
    count = 1
    for char in string[1:] + '\0':  # Add a null terminator to handle the last character
        if char != current_char:
            if current_char:
                encoded.append(f"{count if count > 1 else ''}{current_char}")
            current_char = char
            count = 1
        else:
            count += 1
    return ''.join(encoded)
