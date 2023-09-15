class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"({self.x}, {self.y})"


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                start = Point(row, col)
                for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    end = self.find_word_in_direction(word, start, direction)
                    if end:
                        return (start, end)
        return None

    def find_word_in_direction(self, word, start, direction):
        row, col = start.x, start.y
        d_row, d_col = direction
        if (0 <= row + d_row * (len(word) - 1) < len(self.puzzle) and
                0 <= col + d_col * (len(word) - 1) < len(self.puzzle[row])):
            for i in range(len(word)):
                if self.puzzle[row][col] != word[i]:
                    return None
                row += d_row
                col += d_col
            return Point(row - d_row, col - d_col)
        return None