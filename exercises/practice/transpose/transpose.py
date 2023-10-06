def transpose(lines):
    max_length = max(len(line) for line in lines)
    transposed = []
    for i in range(max_length):
        transposed.append(''.join(lines[j][i] if i < len(lines[j]) else ' ' for j in range(len(lines))))
    return transposed
