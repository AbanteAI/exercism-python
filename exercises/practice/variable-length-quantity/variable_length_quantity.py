def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = []
        while True:
            byte = number & 0x7f
            number >>= 7
            bytes_.append(byte | (0x80 if bytes_ else 0x00))
            if number == 0:
                break
        result.extend(reversed(bytes_))
    return result


def decode(bytes_):
    result = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7f)
        if (byte & 0x80) == 0:
            result.append(number)
            number = 0
    if bytes_ and (bytes_[-1] & 0x80) != 0:
        raise ValueError("incomplete sequence")
    return result
