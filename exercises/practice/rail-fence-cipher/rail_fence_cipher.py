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

    rail_fence = [''] * rails
    length = len(encoded_message)
    index, step = 0, 1

    for _ in range(length):
        rail_fence[index] += 'X'

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    result = [''] * length
    encoded_index = 0

    for i, rail in enumerate(rail_fence):
        for j, char in enumerate(rail):
            if char == 'X':
                rail_fence[i] = rail_fence[i][:j] + encoded_message[encoded_index] + rail_fence[i][j + 1:]
                encoded_index += 1

    index, step = 0, 1

    for _ in range(length):
        result[index] += rail_fence[index][0]
        rail_fence[index] = rail_fence[index][1:]

        if index == 0:
            step = 1
        elif index == rails - 1:
            step = -1

        index += step

    return ''.join(result)