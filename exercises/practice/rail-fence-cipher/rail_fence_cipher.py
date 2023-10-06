def encode(message, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    step = 1
    for char in message:
        fence[rail].append(char)
        rail += step
        if rail == 0 or rail == rails - 1:
            step = -step
    return ''.join(''.join(row) for row in fence)


def decode(encoded_message, rails):
    if rails == 1:
        return encoded_message

    fence = [[] for _ in range(rails)]
    rail = 0
    step = 1

    for _ in encoded_message:
        fence[rail].append(None)
        rail += step
        if rail == 0 or rail == rails - 1:
            step = -step

    i = 0
    for rail in range(rails):
        for j in range(len(fence[rail])):
            if fence[rail][j] is None:
                continue
            fence[rail][j] = encoded_message[i]
            i += 1

    result = []
    rail = 0
    step = 1
    for _ in encoded_message:
        if fence[rail]:
            result.append(fence[rail].pop(0))
        rail += step
        if rail == 0 or rail == rails - 1:
            step = -step

    return ''.join(result)
