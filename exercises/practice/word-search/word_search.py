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
        directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

        for y, row in enumerate(self.puzzle):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    for dx, dy in directions:
                        end_x, end_y = x + (len(word) - 1) * dx, y + (len(word) - 1) * dy
                        if 0 <= end_x < len(row) and 0 <= end_y < len(self.puzzle):
                            end_letter = self.puzzle[end_y][end_x]
                            if end_letter == word[-1]:
                                if all(self.puzzle[y + i * dy][x + i * dx] == word[i] for i in range(len(word))):
                                    return Point(x, y), Point(end_x, end_y)
        return None
