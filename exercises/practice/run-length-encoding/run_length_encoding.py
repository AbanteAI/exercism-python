def decode(string):
    decoded = []
    count = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == '':
                count = '1'
            decoded.append(char * int(count))
            count = ''
    return ''.join(decoded)


def encode(string):
    if not string:
        return ''
    encoded = []
    prev_char = string[0]
    count = 1
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append(f'{count if count > 1 else ""}{prev_char}')
            prev_char = char
            count = 1
    encoded.append(f'{count if count > 1 else ""}{prev_char}')
    return ''.join(encoded)
