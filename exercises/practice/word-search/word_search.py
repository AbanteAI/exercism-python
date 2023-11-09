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
        for direction in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
            for y in range(len(self.puzzle)):
                for x in range(len(self.puzzle[0])):
                    if self._search_from(x, y, word, direction):
                        return (Point(x, y), Point(x + direction[0] * (len(word) - 1), y + direction[1] * (len(word) - 1)))
        return None

    def _search_from(self, x, y, word, direction):
        if x < 0 or y < 0 or x + direction[0] * (len(word) - 1) >= len(self.puzzle[0]) or y + direction[1] * (len(word) - 1) >= len(self.puzzle):
            return False
        for i in range(len(word)):
            if self.puzzle[y + i * direction[1]][x + i * direction[0]] != word[i]:
                return False
        return True
