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
            (0, 1),  # right
            (1, 0),  # down
            (0, -1), # left
            (-1, 0), # up
            (1, 1),  # down-right
            (1, -1), # down-left
            (-1, -1),# up-left
            (-1, 1)  # up-right
        ]

        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[0])):
                for dx, dy in directions:
                    if self._find_word(word, x, y, dx, dy):
                        return (Point(x, y), Point(x + dx * (len(word) - 1), y + dy * (len(word) - 1)))
        return None

    def _find_word(self, word, x, y, dx, dy):
        if x + dx * (len(word) - 1) >= len(self.puzzle[0]) or \
           y + dy * (len(word) - 1) >= len(self.puzzle) or \
           x + dx * (len(word) - 1) < 0 or \
           y + dy * (len(word) - 1) < 0:
            return False

        for i in range(len(word)):
            if self.puzzle[y + dy * i][x + dx * i] != word[i]:
                return False
        return True
