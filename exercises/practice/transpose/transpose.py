def transpose(input_text):
    if not input_text:
        return ""
    lines = input_text.split("\n")
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len, ' ') for line in lines]
    transposed = [''.join(row[::-1]).lstrip()[::-1] for row in zip(*padded_lines[::-1])]
    return "\n".join(transposed)
    return "\n".join(transposed)