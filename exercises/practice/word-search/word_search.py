class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
        self.puzzle = puzzle
        pass

    def search(self, word):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # right, down, diagonal down-right, diagonal down-left
        word_length = len(word)
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                for dx, dy in directions:
                    end_x = i + (word_length - 1) * dx
                    end_y = j + (word_length - 1) * dy
                    if 0 <= end_x < len(self.puzzle) and 0 <= end_y < len(self.puzzle[i]):
                        if word == ''.join(self.puzzle[x][y] for x, y in zip(range(i, end_x + 1, dx), range(j, end_y + 1, dy))):
                            return Point(i, j), Point(end_x, end_y)
        return None, None
