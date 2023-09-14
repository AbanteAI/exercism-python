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
            (1, 0), (0, 1), (-1, 0), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[y])):
                if self.puzzle[y][x] == word[0]:
                    for dx, dy in directions:
                        end_x, end_y = x + (len(word) - 1) * dx, y + (len(word) - 1) * dy
                        if 0 <= end_x < len(self.puzzle[y]) and 0 <= end_y < len(self.puzzle):
                            found = True
                            for i in range(len(word)):
                                if self.puzzle[y + i * dy][x + i * dx] != word[i]:
                                    found = False
                                    break
                            if found:
                                return Point(x, y), Point(end_x, end_y)
        return None
