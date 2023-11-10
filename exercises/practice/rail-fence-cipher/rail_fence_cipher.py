def encode(message, rails):
    # Create a list of strings, one for each rail
    rail_patterns = [''] * rails
    # Determine the direction of movement (downward initially)
    direction = 1
    rail = 0
    # Iterate over each character in the message
    for char in message:
        # Add the character to the current rail
        rail_patterns[rail] += char
        # Change the direction at the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        # Move to the next rail
        rail += direction
    # Join all the rails to get the encoded message
    return ''.join(rail_patterns)


def decode(encoded_message, rails):
    # Calculate the number of characters in each rail
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
    # Split the encoded message into rails
    rails_list = []
    start = 0
    for length in rail_lengths:
        rails_list.append(encoded_message[start:start+length])
        start += length
    # Decode the message by reconstructing the zigzag pattern
    decoded_message = ''
    rail = 0
    direction = 1
    for _ in range(len(encoded_message)):
        decoded_message += rails_list[rail][0]
        rails_list[rail] = rails_list[rail][1:]
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return decoded_message
