def decode(string):
    decoded = []
    count = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == '':
                decoded.append(char)
            else:
                decoded.append(char * int(count))
                count = ''
    return ''.join(decoded)


def encode(string):
    if not string:
        return ''

    encoded = []
    count = 1
    prev_char = string[0]

    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(prev_char)
            count = 1
            prev_char = char

    if count > 1:
        encoded.append(str(count))
    encoded.append(prev_char)

    return ''.join(encoded)
