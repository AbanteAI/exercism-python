class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
        self.puzzle = puzzle

        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    def search(self, word):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

        for y, row in enumerate(self.puzzle):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    for dx, dy in directions:
                        end_x = x + (len(word) - 1) * dx
                        end_y = y + (len(word) - 1) * dy
                        if 0 <= end_x < len(row) and 0 <= end_y < len(self.puzzle):
                            found = True
                            for i in range(len(word)):
                                if self.puzzle[y + i * dy][x + i * dx] != word[i]:
                                    found = False
                                    break
                            if found:
                                return Point(x, y), Point(end_x, end_y)

        return None
