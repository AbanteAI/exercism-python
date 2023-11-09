import re

def decode(string):
    decoded = []
    for count, char in re.findall(r'(\d*)(\D)', string):
        count = int(count) if count else 1
        decoded.append(char * count)
    return ''.join(decoded)


def encode(string):
    encoded = []
    prev_char = ''
    count = 1
    for char in string:
        if char == prev_char:
            count += 1
        else:
            if prev_char:
                encoded.append(f'{count if count > 1 else ""}{prev_char}')
            count = 1
            prev_char = char
    if prev_char:
        encoded.append(f'{count if count > 1 else ""}{prev_char}')
    return ''.join(encoded)
