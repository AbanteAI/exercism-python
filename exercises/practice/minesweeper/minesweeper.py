def annotate(minefield):
    def count_mines_around(minefield, row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r < 0 or r >= len(minefield) or c < 0 or c >= len(minefield[0]):
                    continue
                if minefield[r][c] == "*":
                    count += 1
        return count
    annotated = []
    for row, line in enumerate(minefield):
        annotated_line = ""
        for col, cell in enumerate(line):
            if cell == "*":
                annotated_line += "*"
            else:
                count = count_mines_around(minefield, row, col)
                annotated_line += str(count) if count > 0 else " "
        annotated.append(annotated_line)
    return annotated
