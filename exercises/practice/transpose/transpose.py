def transpose(input_text):
    lines = input_text.split("\n")
    if not lines:
        return ""
    max_length = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_length, ' ') for line in lines]
    transposed = [''.join(row).rstrip() for row in zip(*padded_lines)]
    return "\n".join(transposed)