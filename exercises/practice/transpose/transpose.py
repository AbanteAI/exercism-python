def transpose(lines):
    if not lines:
        return ""

    # Split the input text into lines
    lines = lines.split('\n')

    # Find the maximum line length
    max_length = max(len(line) for line in lines)

    # Transpose the lines with left padding
    transposed_lines = []
    for i in range(max_length):
        # Extract the ith character from each line, if available
        transposed_line = ''
        for line in lines:
            transposed_line += line[i] if i < len(line) else ' '
        # Right strip the transposed line to remove trailing spaces
        transposed_lines.append(transposed_line.rstrip())

    # Join the transposed lines into a single string with newlines
    return '\n'.join(transposed_lines)
