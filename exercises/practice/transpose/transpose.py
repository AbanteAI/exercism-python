def transpose(lines):
    if not lines:
        return lines

    lines = lines.split("\n")
    max_length = max(len(line) for line in lines)

    # Pad lines with spaces to make them of equal length
    lines = [line.ljust(max_length) for line in lines]

    result = ["".join(line[i] for line in lines).rstrip() for i in range(max_length)]
    return "\n".join(result)