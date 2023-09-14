def encode(numbers):
    encoded = []
    for number in numbers:
        bytes_ = []
        while True:
            bytes_.insert(0, number & 0x7F)
            number >>= 7
            if not number:
                break
        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80
        encoded.extend(bytes_)
    return encoded

def decode(bytes_):
    decoded = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if not byte & 0x80:
            decoded.append(number)
            number = 0
    if number:
        raise ValueError("incomplete sequence")
    return decoded