def encode(message, rails):
    if rails == 1 or rails >= len(message):
        return message

    fence = [''] * rails
    index, step = 0, 1

    for char in message:
        fence[index] += char

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    return ''.join(fence)


def decode(encoded_message, rails):
    if rails == 1 or rails >= len(encoded_message):
        return encoded_message

    fence = [''] * rails
    index, step = 0, 1
    for char in encoded_message:
        fence[index] += char

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    fence = [list(rail) for rail in fence]
    decoded_message = []

    index, step = 0, 1
    for _ in range(len(encoded_message)):
        decoded_message.append(fence[index].pop(0))

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    return ''.join(decoded_message)
