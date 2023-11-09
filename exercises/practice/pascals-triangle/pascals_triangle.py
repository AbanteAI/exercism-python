def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]

    def generate_row(previous_row):
        return [1] + [previous_row[i] + previous_row[i + 1] for i in range(len(previous_row) - 1)] + [1]

    previous_rows = rows(row_count - 1)
    last_row = generate_row(previous_rows[-1])
    return previous_rows + [last_row]
