def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    triangle = []
    for i in range(row_count):
        row = [1]
        if i > 0:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row[:-1], last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle