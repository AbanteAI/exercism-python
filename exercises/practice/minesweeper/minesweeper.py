def annotate(minefield):
def annotate(minefield):
    rows = len(minefield)
    cols = len(minefield[0])
    counts = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == ' ':
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (0 <= i + x < rows) and (0 <= j + y < cols) and minefield[i + x][j + y] == '*':
                            count += 1
                if count > 0:
                    counts[i][j] = str(count)
                else:
                    counts[i][j] = ' '
            else:
                counts[i][j] = minefield[i][j]
    
    return counts
    pass
