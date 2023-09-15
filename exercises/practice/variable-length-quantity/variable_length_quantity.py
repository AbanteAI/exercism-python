def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = []
        while True:
            byte = number & 0x7F
            number >>= 7
            bytes_.insert(0, byte | 0x80 if bytes_ else byte)
            if number == 0:
                break
        result.extend(bytes_)
    return result


def decode(bytes_):
    result = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if not (byte & 0x80):
            result.append(number)
            number = 0
        elif byte == 0x80:
            raise ValueError("incomplete sequence")
    if number:
        raise ValueError("incomplete sequence")
        raise ValueError("incomplete sequence")
    return result
