def encode(numbers):
def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = [number & 0x7F]
        number >>= 7
        while number:
            bytes_.insert(0, 0x80 | (number & 0x7F))
            number >>= 7
        result.extend(bytes_)
    return result

def decode(bytes_):
def decode(bytes_):
    result = []
    current = 0
    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        if not byte & 0x80:
            result.append(current)
            current = 0
    if current:
        raise ValueError("incomplete sequence")
    return result