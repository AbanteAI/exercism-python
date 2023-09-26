def encode(message, rails):
    if rails == 1:
        return message

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    encoded_message = ""
    for rail in fence:
        encoded_message += "".join(rail)

    return encoded_message


def decode(encoded_message, rails):
    if rails == 1:
        return encoded_message

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

        fence[rail][i] = encoded_message[index]
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = None
            rail[i] = None

    rail = 0
    direction = 1
    decoded_message = ""

        decoded_message += fence[rail][0]
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return decoded_message
