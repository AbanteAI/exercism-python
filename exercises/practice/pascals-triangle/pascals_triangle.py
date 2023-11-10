def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]

    previous_row = rows(row_count - 1)
    last_row = previous_row[-1]
    current_row = [1]

    for i in range(1, len(last_row)):
        current_row.append(last_row[i - 1] + last_row[i])
    current_row.append(1)

    return previous_row + [current_row]