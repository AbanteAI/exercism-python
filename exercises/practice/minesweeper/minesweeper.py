def annotate(minefield):
    def count_adjacent_mines(row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (
                    0 <= r < len(minefield)
                    and 0 <= c < len(minefield[0])
                    and minefield[r][c] == "*"
                ):
                    count += 1
        return count

    annotated_minefield = []
    for row, line in enumerate(minefield):
        annotated_line = ""
        for col, cell in enumerate(line):
            if cell == "*":
                annotated_line += "*"
            else:
                count = count_adjacent_mines(row, col)
                annotated_line += str(count) if count > 0 else " "
        annotated_minefield.append(annotated_line)
    return annotated_minefield