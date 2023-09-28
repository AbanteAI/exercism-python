def encode(message, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    encoded_message = ''.join([''.join(row) for row in fence])
    return encoded_message


def decode(encoded_message, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for _ in encoded_message:
        fence[rail].append(None)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for rail in range(rails):
        for i in range(len(fence[rail])):
            if fence[rail][i] is None:
                fence[rail][i] = encoded_message[index]
                index += 1

    decoded_message = []
    rail = 0
    direction = 1

    for _ in encoded_message:
        decoded_message.append(fence[rail].pop(0))
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return ''.join(decoded_message)
