def decode(string):
    decoded = ""
    count = 0
    for char in string:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decoded += char * (count if count > 0 else 1)
            count = 0
    return decoded


def encode(string):
    encoded = ""
    count = 1
    prev_char = string[0] if string else None
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded += (str(count) if count > 1 else "") + prev_char
            prev_char = char
            count = 1
    encoded += (str(count) if count > 1 else "") + prev_char if prev_char else ""
    return encoded
