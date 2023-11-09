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
            (-1, -1),# up-left
            (1, -1), # down-left
            (-1, 1)  # up-right
        ]
        for y, row in enumerate(self.puzzle):
            for x, char in enumerate(row):
                if char == word[0]:
                    for dx, dy in directions:
                        end_x, end_y = x, y
                        for i in range(1, len(word)):
                            end_x += dx
                            end_y += dy
                            if not (0 <= end_x < len(row) and 0 <= end_y < len(self.puzzle)):
                                break
                            if self.puzzle[end_y][end_x] != word[i]:
                                break
                        else:
                            return Point(x, y), Point(end_x, end_y)
        return None
