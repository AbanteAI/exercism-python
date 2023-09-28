def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = []
        while True:
            bytes_.insert(0, number & 0x7F)
            number >>= 7
            if number == 0:
                break
        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80
        result.extend(bytes_)
    return result


def decode(bytes_):
    result = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            result.append(number)
            number = 0
        elif byte == bytes_[-1]:
            raise ValueError("incomplete sequence")
    return result
