class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        directions = [
            (0, 1),     # right
            (0, -1),    # left
            (1, 0),     # down
            (-1, 0),    # up
            (1, 1),     # diagonal down-right
            (1, -1),    # diagonal down-left
            (-1, 1),    # diagonal up-right
            (-1, -1)    # diagonal up-left
        ]

        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        for row in range(rows):
            for col in range(cols):
                for direction in directions:
                    x, y = row, col
                    dx, dy = direction
                    found = True

                    for char in word:
                        if x < 0 or x >= rows or y < 0 or y >= cols or self.puzzle[x][y] != char:
                            found = False
                            break

                        x += dx
                        y += dy

                    if found:
                        start = Point(col, row)
                        end = Point(y - dy, x - dx)
                        return start, end

        return None
