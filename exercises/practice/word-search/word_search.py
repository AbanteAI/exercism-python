class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i in range(rows):
            for j in range(cols):
                for direction in directions:
                    dx, dy = direction
                    x, y = i, j
                    found = True
                    for letter in word:
                        if x < 0 or x >= rows or y < 0 or y >= cols or self.puzzle[x][y] != letter:
                            found = False
                            break
                        x += dx
                        y += dy
                    if found:
                        return Point(j, i), Point(y - dy, x - dx)
        return None, None