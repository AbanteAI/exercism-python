def decode(string):
    decoded = ""
    count = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == "":
                decoded += char
            else:
                decoded += int(count) * char
                count = ""
    return decoded


def encode(string):
    encoded = ""
    count = 1
    prev_char = string[0] if string else ""
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded += (str(count) if count > 1 else "") + prev_char
            count = 1
            prev_char = char
    encoded += (str(count) if count > 1 else "") + prev_char
    return encoded
