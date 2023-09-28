def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        bytes_ = []
        while True:
            bytes_.append(number & 0x7F)
            if number < 128:
                break
            number >>= 7
        for i in range(len(bytes_) - 1, 0, -1):
            bytes_[i] |= 0x80
        encoded_bytes.extend(bytes_)
    return bytes(encoded_bytes)


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            numbers.append(number)
            number = 0
    return numbers


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            numbers.append(number)
            number = 0
    return numbers