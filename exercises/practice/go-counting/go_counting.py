
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board

    def territory(self, x, y):
        owner = self.board[y][x]
        visited = set()
        territories = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(self.board[0]) or y >= len(self.board) or (x, y) in visited:
                return
            visited.add((x, y))
            if self.board[y][x] == owner:
                territories.add((x, y))
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        dfs(x, y)
        return (owner, territories)

    def territories(self):
        result = {"W": set(), "B": set(), "": set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == "W" or self.board[y][x] == "B":
                    owner, territories = self.territory(x, y)
                    result[owner].update(territories)
        return result

        dfs(x, y)
        return (owner, territories)

    def territories(self):
        result = {"W": set(), "B": set(), "": set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == "W" or self.board[y][x] == "B":
                    owner, territories = self.territory(x, y)
                    result[owner].update(territories)
        return result

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        pass
