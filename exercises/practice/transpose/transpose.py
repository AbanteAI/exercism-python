def transpose(input_text):
    if not input_text:
        return input_text

    lines = input_text.split('\n')
    max_length = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_length) for line in lines]
    transposed = [''.join(row).rstrip() for row in zip(*padded_lines)]

    # Ensure the last line has no extra spaces if it's all spaces
    if transposed and set(transposed[-1]) == {' '}:
        transposed[-1] = ''

    return '\n'.join(transposed)
