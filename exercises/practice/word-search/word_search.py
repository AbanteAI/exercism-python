class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
            (-1, 1),  # diagonal up-right
            (-1, -1)  # diagonal up-left
        ]

        width = len(self.puzzle[0])
        height = len(self.puzzle)

        for y in range(height):
            for x in range(width):
                for direction in directions:
                    dx, dy = direction
                    end_x = x + (len(word) - 1) * dx
                    end_y = y + (len(word) - 1) * dy

                    if 0 <= end_x < width and 0 <= end_y < height:
                        if all(self.puzzle[y + i * dy][x + i * dx] == word[i] for i in range(len(word))):
                            return Point(x, y), Point(end_x, end_y)

        return None, None
