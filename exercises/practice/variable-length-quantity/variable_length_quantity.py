def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        bytes_ = []
        while True:
            byte = number & 0x7F
            number >>= 7
            if number != 0:
                byte |= 0x80
            bytes_.append(byte)
            if number == 0:
                break
        encoded_bytes.extend(bytes_[::-1])
    return encoded_bytes


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            numbers.append(number)
            number = 0
    return numbers