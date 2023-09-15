
class Board:
WHITE = "W"
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        pass

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        owner = self.board[y][x]
        territories = set()
        visited = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(self.board[0]) or y >= len(self.board) or (x, y) in visited:
                return
            visited.add((x, y))
            if self.board[y][x] == owner:
                territories.add((x, y))
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)

        dfs(x, y)
        return owner, territories

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        owners = {"W": set(), "B": set(), "": set()}
        visited = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(self.board[0]) or y >= len(self.board) or (x, y) in visited:
                return
            visited.add((x, y))
            owner, territories = self.territory(x, y)
            owners[owner].update(territories)
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if (x, y) not in visited:
                    dfs(x, y)

        return owners
