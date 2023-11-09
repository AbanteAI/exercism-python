def encode(message, rails):
    # Create a list of strings, one for each rail
    rail_patterns = [''] * rails
    # Determine the direction of movement (downward initially)
    direction = 1
    rail = 0

    # Iterate over each character in the message
    for char in message:
        # Place the character in the current rail
        rail_patterns[rail] += char
        # Change the direction at the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        # Move to the next rail
        rail += direction

    # Concatenate all the rails to get the encoded message
    return ''.join(rail_patterns)


def decode(encoded_message, rails):
    # Calculate the length of the encoded message
    n = len(encoded_message)
    # Create a list to hold the decoded message
    decoded_message = [''] * n
    # Create a list to hold the indices of the characters in the rail pattern
    indices = []

    # Determine the order of indices for each rail
    rail = 0
    for _ in range(rails):
        i = rail
        direction = 1
        while i < n:
            indices.append(i)
            if rail == 0:
                direction = 1
            elif rail == rails - 1:
                direction = -1
            # Determine the next index based on the current direction
            i += (rails - 1) * 2 if direction == 1 else 2
        rail += 1

    # Sort the indices by the order they appear in the rail pattern
    order = sorted(range(n), key=lambda i: indices.index(i))

    # Place the characters in the decoded message according to the rail pattern
    for i, char in zip(order, encoded_message):
        decoded_message[i] = char

    # Join the characters to get the decoded message
    return ''.join(decoded_message)
