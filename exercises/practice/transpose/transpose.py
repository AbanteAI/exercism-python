def transpose(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')

    if not lines:
        return ''

    # Find the maximum length of the lines to determine the width of the transpose
    max_length = max(len(line) for line in lines)

    # Pad lines with spaces to have the same width
    padded_lines = [line.ljust(max_length) for line in lines]

    # Transpose the lines
    transposed = [''.join(row).rstrip() for row in zip(*padded_lines)]

    # Remove trailing spaces from the last line if it's all spaces
    if transposed and set(transposed[-1]) == {' '}:
        transposed[-1] = ''

    # Join the transposed lines into a single string
    return '\n'.join(transposed)
