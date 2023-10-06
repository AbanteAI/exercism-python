def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = []
        while True:
            byte = number & 0x7F
            number >>= 7
            bytes_.insert(0, byte | (0x80 if bytes_ else 0))
            if not number:
                break
        result.extend(bytes_)
    return result


def decode(bytes_):
    result = []
    current = 0
    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        if not byte & 0x80:
            result.append(current)
            current = 0
        elif byte == bytes_[-1]:
            raise ValueError("incomplete sequence")
    return result
