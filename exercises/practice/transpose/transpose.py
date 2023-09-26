def transpose(lines):
    if not lines:
        return []
    lines = [line.ljust(max_length) for line in lines]
    transposed = ["".join(row) for row in zip(*lines)]
    return transposed
