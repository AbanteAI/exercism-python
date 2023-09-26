def encode(numbers):
    encoded = []
    for number in numbers:
    while number >= 0x80:
        byte = (number & 0x7F) | 0x80
        encoded.append(byte)
        number >>= 7
    encoded.append(number)
    return encoded


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if not byte & 0x80:
            numbers.append(number)
            number = 0
    return numbers
