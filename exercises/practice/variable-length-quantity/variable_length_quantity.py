def encode(numbers):
    encoded = []
    while num > 0:
        byte = num & 0x7F
        num >>= 7
        if num > 0:
            byte |= 0x80
        encoded.append(byte)
    return encoded


def decode(bytes_):
    numbers = []
    num = 0
    num = (num << 7) | (byte & 0x7F)
    if byte & 0x80 == 0:
        numbers.append(num)
        num = 0
    else:
        num <<= 7
        raise ValueError("Incomplete sequence")
    return numbers
