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
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(rows):
            for j in range(cols):
                if self.puzzle[i][j] == word[0]:
                    for direction in directions:
                        x, y = i, j
                        found = True
                        for char in word[1:]:
                            x += direction[0]
                            y += direction[1]
                            if x < 0 or x >= rows or y < 0 or y >= cols or self.puzzle[x][y] != char:
                                found = False
                                break
                        if found:
                            start = Point(j, i)
                            end = Point(y, x)
                            return start, end
        return None, None
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(rows):
            for j in range(cols):
                if self.puzzle[i][j] == word[0]:
                    for direction in directions:
                        x, y = i, j
                        found = True
                        for char in word[1:]:
                            x += direction[0]
                            y += direction[1]
                            if x < 0 or x >= rows or y < 0 or y >= cols or self.puzzle[x][y] != char:
                                found = False
                                break
                        if found:
                            start = Point(j, i)
                            end = Point(y, x)
                            return start, end
        return None, None