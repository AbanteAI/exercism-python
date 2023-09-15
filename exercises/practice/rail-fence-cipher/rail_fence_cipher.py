def encode(message, rails):
    encoded_message = ""
    rail_lines = [[] for _ in range(rails)]
    direction = 1
    rail_index = 0

    for char in message:
        rail_lines[rail_index].append(char)

        if rail_index == 0:
            direction = 1
        elif rail_index == rails - 1:
            direction = -1

        rail_index += direction

    for rail_line in rail_lines:
        encoded_message += "".join(rail_line)

    return encoded_message


def decode(encoded_message, rails):
    decoded_message = ""
    rail_lines = [[] for _ in range(rails)]
    direction = 1
    rail_index = 0

    for char in encoded_message:
        rail_lines[rail_index].append(None)

        if rail_index == 0:
            direction = 1
        elif rail_index == rails - 1:
            direction = -1

        rail_index += direction

    index = 0
    for rail_line in rail_lines:
        for i in range(len(rail_line)):
            rail_line[i] = encoded_message[index]
            index += 1

    rail_index = 0
    direction = 1

    for _ in range(len(encoded_message)):
        decoded_message += rail_lines[rail_index].pop(0)

        if rail_index == 0:
            direction = 1
        elif rail_index == rails - 1:
            direction = -1

        rail_index += direction

    return decoded_message


def decode(encoded_message, rails):
    pass
