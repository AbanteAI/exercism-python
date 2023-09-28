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
    encoded = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(string[i - 1])
            count = 1

    if count > 1:
        encoded.append(str(count))
    if string:
        encoded.append(string[-1])

    return ''.join(encoded)
