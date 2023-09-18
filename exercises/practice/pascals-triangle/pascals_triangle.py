def rows(row_count):
    if row_count < 0:
        raise ValueError("Row count must be non-negative")

    result = []
    for i in range(row_count):
        row = [1]
        if result:
            last_row = result[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        result.append(row)
    return result