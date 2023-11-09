def encode(message, rails):
    # Create a list of strings, one for each rail
    rail_pattern = [''] * rails
    # Determine the direction of movement (downward initially)
    direction = 1
    # Start at the top rail
    rail = 0

    # Iterate over each character in the message
    for char in message:
        # Add the character to the current rail
        rail_pattern[rail] += char
        # Change the rail according to the direction
        rail += direction
        # If we hit the top or bottom, reverse direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Combine all the rails to form the encoded message
    return ''.join(rail_pattern)


def decode(encoded_message, rails):
    # Calculate the number of characters in each rail
    rail_lengths = [0] * rails
    direction = 1
    rail = 0
    for char in encoded_message:
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Create a list of strings, one for each rail, filled with the encoded message
    rails_list = []
    idx = 0
    for length in rail_lengths:
        rails_list.append(encoded_message[idx:idx + length])
        idx += length

    # Decode the message by reconstructing the zig-zag pattern
    decoded_message = ''
    direction = 1
    rail = 0
    for _ in range(len(encoded_message)):
        decoded_message += rails_list[rail][0]
        rails_list[rail] = rails_list[rail][1:]
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return decoded_message
