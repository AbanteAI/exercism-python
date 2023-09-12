def transpose(lines):
def transpose(lines):
    if not lines:
        return lines

    rows = lines.split("\n")
    max_length = max(len(row) for row in rows)
    result = []

    for i in range(max_length):
        new_row = []
        for row in rows:
            if i < len(row):
                new_row.append(row[i])
            else:
                new_row.append(" ")
        result.append("".join(new_row).rstrip())

    return "\n".join(result)
