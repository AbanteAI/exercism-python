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
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for y, row in enumerate(self.puzzle):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    for dx, dy in directions:
                        x_end, y_end = x + (len(word) - 1) * dx, y + (len(word) - 1) * dy

                        if 0 <= x_end < len(row) and 0 <= y_end < len(self.puzzle):
                            if all(self.puzzle[y + k * dy][x + k * dx] == word[k] for k in range(len(word))):
                                return Point(x, y), Point(x_end, y_end)
        return None
