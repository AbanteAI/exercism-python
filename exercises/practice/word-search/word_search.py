class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
        self.puzzle = puzzle

        # Search for the word in all directions
        for direction in self._directions():
            start_point, end_point = self._search_in_direction(word, direction)
            if start_point and end_point:
                return (start_point, end_point)
        return None

    def _directions(self):
        # Returns a list of directions to search in the form of (dx, dy)
        return [
            (0, 1),  # Left to right
            (1, 0),  # Top to bottom
            (0, -1), # Right to left
            (-1, 0), # Bottom to top
            (1, 1),  # Top left to bottom right
            (-1, -1),# Bottom right to top left
            (1, -1), # Top right to bottom left
            (-1, 1), # Bottom left to top right
        ]

    def _search_in_direction(self, word, direction):
        # Search for the word in the given direction
        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[y])):
                if self._starts_at(word, x, y, direction):
                    start_point = Point(x, y)
                    end_x = x + direction[0] * (len(word) - 1)
                    end_y = y + direction[1] * (len(word) - 1)
                    end_point = Point(end_x, end_y)
                    return (start_point, end_point)
        return (None, None)

    def _starts_at(self, word, x, y, direction):
        # Check if the word starts at the (x, y) position in the given direction
        for i in range(len(word)):
            dx = x + i * direction[0]
            dy = y + i * direction[1]
            if dx < 0 or dy < 0 or dy >= len(self.puzzle) or dx >= len(self.puzzle[dy]) or self.puzzle[dy][dx] != word[i]:
                return False
        return True
