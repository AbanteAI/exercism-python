def transpose(input_text):
    if not input_text:
        return ""

    lines = input_text.split('\n')
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    transposed = []
    for i in range(max_len):
        transposed_line = ''.join(line[i] for line in padded_lines)
        transposed.append(transposed_line.rstrip())

    return '\n'.join(transposed)