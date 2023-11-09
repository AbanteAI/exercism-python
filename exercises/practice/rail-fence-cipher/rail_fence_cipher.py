def encode(message, rails):
    # Create a list of strings, one for each rail
    rail_patterns = [''] * rails
    # Determine the direction of movement (down or up the rails)
    direction = 1  # Start by moving 'down'
    rail = 0  # Start at the top rail

    # Iterate over each character in the message
    for char in message:
        # Add the character to the current rail
        rail_patterns[rail] += char
        # Change the direction if we hit the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        # Move to the next rail
        rail += direction

    # Combine the strings from each rail to get the encoded message
    return ''.join(rail_patterns)


def decode(encoded_message, rails):
    # Calculate the number of characters on each rail
    rail_lengths = [0] * rails
    direction = 1
    rail = 0
    for char in encoded_message:
        rail_lengths[rail] += 1
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    # Split the encoded message into strings for each rail
    rail_strings = []
    pos = 0
    for length in rail_lengths:
        rail_strings.append(encoded_message[pos:pos + length])
        pos += length

    # Reconstruct the original message by zig-zagging through the rails
    result = []
    direction = 1
    rail = 0
    for _ in encoded_message:
        # Take the next character from the current rail
        result.append(rail_strings[rail][0])
        rail_strings[rail] = rail_strings[rail][1:]
        # Change the direction if we hit the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        # Move to the next rail
        rail += direction

    # Combine the characters to get the decoded message
    return ''.join(result)
