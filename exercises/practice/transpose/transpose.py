def transpose(lines):
    if not lines:
        return []
    max_length = max(len(line) for line in lines)
    transposed_lines = []
    for i in range(max_length):
        transposed_line = []
        for line in lines:
            if i < len(line):
                transposed_line.append(line[i])
            else:
                transposed_line.append(' ')
        transposed_lines.append(''.join(transposed_line))
    return transposed_lines