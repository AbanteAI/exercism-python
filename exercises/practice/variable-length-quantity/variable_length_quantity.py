def encode(numbers):
    encoded = []
    for number in numbers:
        bytes_ = []
    for number in numbers:
        bytes_ = []
        while True:
            bytes_.insert(0, number & 0x7F)
            number >>= 7
            if number == 0:
                break
        bytes_[-1] |= 0x80
        encoded.extend(bytes_)
        encoded.extend(bytes_)
    return encoded


    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            numbers.append(number)
            number = 0
    if number != 0:
        raise ValueError("Invalid variable length quantity")
    return numbers
