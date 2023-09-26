
from go_counting_constants import WHITE, BLACK, EMPTY
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = [[WHITE if c == 'O' else BLACK if c == 'X' else EMPTY for c in row] for row in board]

    def territory(self, x, y):
        if self.board[y][x] != EMPTY:
            return "", set()

        def dfs(x, y, visited):
            if x < 0 or x >= len(self.board[0]) or y < 0 or y >= len(self.board) or (x, y) in visited:
                return
            visited.add((x, y))
            if self.board[y][x] == EMPTY:
                return
            if self.board[y][x] == WHITE:
                self.territories["O"].add((x, y))
            if self.board[y][x] == BLACK:
                self.territories["X"].add((x, y))
            dfs(x + 1, y, visited)
            dfs(x - 1, y, visited)
        self.territories = {WHITE: set(), BLACK: set()}
            dfs(x, y - 1, visited)
            if len(self.territories[WHITE]) > 0 and len(self.territories[BLACK]) > 0:
        self.territories = {"O": set(), "X": set()}
            if len(self.territories
        if len(self.territories["O"]) > 0 and len(self.territories["X"]) > 0:
            return "", set()
        if len(self.territories["O"]) > 0:
            return "O", self.territories["O"]
        if len(self.territories["X"]) > 0:
            return "X", self.territories["X"]
        return "", set()

    def territories(self):
        self.territories = {"O": set(), "X": set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                owner, territory = self.territory(x, y)
                if owner:
                    self.territories[owner].update(territory)
        return self.territories
