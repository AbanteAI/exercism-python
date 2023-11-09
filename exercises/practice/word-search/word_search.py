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
        directions = [
            (0, 1), (1, 0), (1, 1), (1, -1),
            (0, -1), (-1, 0), (-1, -1), (-1, 1)
        ]
        for y, row in enumerate(self.puzzle):
            for x, char in enumerate(row):
                if char == word[0]:
                    for dx, dy in directions:
                        if self._check_word(word, x, y, dx, dy):
                            end_x = x + dx * (len(word) - 1)
                            end_y = y + dy * (len(word) - 1)
                            return Point(x, y), Point(end_x, end_y)
        return None

    def _check_word(self, word, x, y, dx, dy):
        for i in range(len(word)):
            if not (0 <= x + dx * i < len(self.puzzle[0]) and 0 <= y + dy * i < len(self.puzzle)):
                return False
            if self.puzzle[y + dy * i][x + dx * i] != word[i]:
                return False
        return True
