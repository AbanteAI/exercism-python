def transpose(lines):
    if not lines:
        return []
    transposed_lines = []
    for i in range(max_length):
    transposed_lines = []
    max_length = max(len(line) for line in lines)
    for i in range(max_length):
        transposed_line = ""
        for line in lines:
            if i < len(line):
                transposed_line += line[i]
            else:
                transposed_line += " "
        transposed_lines.append(transposed_line)
    return transposed_lines
        transposed_lines.append(transposed_line)
    return transposed_lines