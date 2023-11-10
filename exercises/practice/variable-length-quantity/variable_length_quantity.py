def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        if number == 0:
            encoded_bytes.append(0)
        else:
            bytes_list = []
            while number > 0:
                byte = number & 0x7F
                number >>= 7
                bytes_list.insert(0, byte | 0x80)
            bytes_list[-1] &= 0x7F
            encoded_bytes.extend(bytes_list)
    return encoded_bytes

def decode(bytes_):
    if not bytes_ or (bytes_[-1] & 0x80) != 0:
        raise ValueError("incomplete sequence")

    numbers = []
    number = 0
    for byte in bytes_:
        number = (number << 7) | (byte & 0x7F)
        if (byte & 0x80) == 0:
            numbers.append(number)
            number = 0
    return numbers