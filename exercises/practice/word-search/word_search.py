class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

        for _ in range(word_length):
            if x < 0 or x >= len(self.puzzle) or y < 0 or y >= len(self.puzzle[row]) or self.puzzle[x][y] != word[_]:
                break
            x += direction[0]
            y += direction[1]
        else:
            start = Point(col, row)
            end = Point(y - direction[1], x - direction[0])
            return start, end
        return None
    def __init__(self, puzzle):
        pass

    def search(self, word):
        pass
