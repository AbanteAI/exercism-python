def encode(message, rails):
    if rails == 1 or rails >= len(message):
        return message

    result = [''] * rails
    index, step = 0, 1

    for char in message:
        result[index] += char

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    return ''.join(result)


def decode(encoded_message, rails):
    if rails == 1 or rails >= len(encoded_message):
        return encoded_message

    result = [''] * rails
    lengths = [0] * rails
    index, step = 0, 1

    for _ in encoded_message:
        lengths[index] += 1

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    current_index = 0
    for i in range(rails):
        result[i] = encoded_message[current_index:current_index + lengths[i]]
        current_index += lengths[i]

    decoded_message = []
    index, step = 0, 1
    for _ in encoded_message:
        decoded_message.append(result[index][0])
        result[index] = result[index][1:]

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    return ''.join(decoded_message)
