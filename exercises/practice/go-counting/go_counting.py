
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    self.board = board
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
        if self.board[y][x] != ' ':
            raise ValueError('Invalid coordinate')

        owner = self.board[y][x]
        territories = set()
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= len(self.board[0]) or y < 0 or y >= len(self.board):
                return
            if (x, y) in visited or self.board[y][x] != owner:
                return
            visited.add((x, y))
            territories.add((x, y))
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        dfs(x, y)

        return owner, territories
