def transpose(lines):
def transpose(lines):
    if not lines:
        return []

    # Pad rows with spaces to match the length of the longest row
    max_length = max(len(row) for row in lines)
    padded_lines = [row.ljust(max_length) for row in lines]

    # Transpose the matrix
    transposed = [''.join(row[i] for row in padded_lines).rstrip() for i in range(max_length)]

    return transposed
