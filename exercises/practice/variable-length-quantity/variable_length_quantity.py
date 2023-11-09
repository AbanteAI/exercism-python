def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        bytes_of_number = []
        while True:
            byte = number & 0x7F
            number >>= 7
            if bytes_of_number:
                byte |= 0x80
            bytes_of_number.insert(0, byte)
            if number == 0:
                break
        encoded_bytes.extend(bytes_of_number)
    return encoded_bytes


def decode(bytes_):
    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            numbers.append(number)
            number = 0
    if byte & 0x80 != 0:
        raise ValueError("incomplete sequence")
    return numbers
