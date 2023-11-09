def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        if number == 0:
            encoded_bytes.append(0)
        else:
            bytes_chunk = []
            while number > 0:
                byte = number & 0x7F
                number >>= 7
                bytes_chunk.insert(0, byte | 0x80)
            bytes_chunk[-1] &= 0x7F
            encoded_bytes.extend(bytes_chunk)
    return encoded_bytes


def decode(bytes_):
    numbers = []
    value = 0
    for byte in bytes_:
        value = (value << 7) | (byte & 0x7F)
        if (byte & 0x80) == 0:
            numbers.append(value)
            value = 0
    if (byte & 0x80) != 0:
        raise ValueError("incomplete sequence")
    return numbers