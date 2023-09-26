def decode(string):
    decoded_string = ""
    count = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            decoded_string += char * (int(count) if count else 1)
            count = ""
    return decoded_string


def encode(string):
    encoded_string = ""
    count = 1
    for i in range(len(string)):
        if i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
        else:
            if count > 1:
                encoded_string += str(count)
            encoded_string += string[i]
            count = 1
    return encoded_string
