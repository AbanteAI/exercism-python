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

    fence = [[] for _ in range(rails)]
    index, step = 0, 1

    for _ in encoded_message:
        fence[index].append(None)

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    index = 0
    for i, s in enumerate(encoded_message):
        fence[index][fence[index].index(None)] = s

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    result = ''
    index, step = 0, 1
    for row in fence:
        for char in row:
            if char:
                result += char

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    return result
                    step = 1
                elif index == rails - 1:
                    step = -1

                index += step

    return result
