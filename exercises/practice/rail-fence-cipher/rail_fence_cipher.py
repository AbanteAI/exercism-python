    if rails == 1:
        return message

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    encoded_message = ""
    for rail in fence:
        encoded_message += "".join(rail)

    return encoded_message

        return encoded_message

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in encoded_message:
        fence[rail].append(None)

    for _ in range(len(encoded_message)):
        fence[rail].pop()
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    rail_lengths = [len(rail) for rail in fence]
    decoded_message = ""
    rail_index = 0

    for char in encoded_message:
        decoded_message += char
        if len(decoded_message) == rail_lengths[rail_index]:
            rail_index += 1

    return decoded_message
