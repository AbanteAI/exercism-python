def annotate(minefield):
    if not minefield:
        return minefield

    if any(len(row) != len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")

    if any(char not in " *." for row in minefield for char in row):
        raise ValueError("The board is invalid with current input.")

    def count_mines(x, y):
        return sum(
            minefield[x + dx][y + dy] == "*"
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if 0 <= x + dx < len(minefield) and 0 <= y + dy < len(minefield[0])
        )

    annotated = [
        [
            "*" if cell == "*" else str(count_mines(x, y))
            for y, cell in enumerate(row)
        ]
        for x, row in enumerate(minefield)
    ]

    return ["".join(row) for row in annotated]