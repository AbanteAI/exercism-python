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
        for y, row in enumerate(self.puzzle):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    for direction in ((0, 1), (1, 0), (1, 1), (-1, 1)):
                        end_x, end_y = x + (len(word) - 1) * direction[0], y + (len(word) - 1) * direction[1]
                        if 0 <= end_x < len(row) and 0 <= end_y < len(self.puzzle):
                            if all(self.puzzle[y + step * direction[1]][x + step * direction[0]] == word[step] for step in range(len(word))):
                                return Point(x, y), Point(end_x, end_y)
        return None
