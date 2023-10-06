def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    else:
        previous_rows = rows(row_count - 1)
        previous_row = previous_rows[-1]
        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        previous_rows.append(current_row)
        return previous_rows
