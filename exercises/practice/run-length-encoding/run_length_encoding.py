def decode(string):
    decoded = ""
    count = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            decoded += char * (int(count) if count else 1)
            count = ""
    return decoded


def encode(string):
    if not string:
        return ""
    encoded = ""
    current_char = string[0]
    count = 1
    for char in string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded += (str(count) if count > 1 else "") + current_char
            current_char = char
            count = 1
    encoded += (str(count) if count > 1 else "") + current_char
    return encoded
