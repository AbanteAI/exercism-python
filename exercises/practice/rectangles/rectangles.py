def rectangles(strings):
    def count_corners(x, y):
        return sum(1 for a in range(y + 1, len(strings))
                   for b in range(x + 1, len(strings[0]))
                   if strings[y][x] == '+' and strings[y][b] == '+' and strings[a][x] == '+' and strings[a][b] == '+'
                   and all(strings[y][i] in '+-' for i in range(x + 1, b))
                   and all(strings[a][i] in '+-' for i in range(x + 1, b))
                   and all(strings[i][x] in '+|' for i in range(y + 1, a))
                   and all(strings[i][b] in '+|' for i in range(y + 1, a)))

    return sum(count_corners(x, y) for y in range(len(strings)) for x in range(len(strings[0])) if strings[y][x] == '+')