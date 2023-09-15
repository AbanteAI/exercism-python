WHITE = "W"
BLACK = "B"
NONE = ""

class Board:
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
        if not (0 <= x < len(self.board[0]) and 0 <= y < len(self.board)):
            return None, set()
        if self.board[y][x] in "BW":
            return None, set()
        visited = set()
        stack = [(x, y)]
        owner = None
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(self.board[0]) and 0 <= ny < len(self.board)):
                    if self.board[ny][nx] in "BW":
                        if owner is None:
                            owner = self.board[ny][nx]
                        elif owner != self.board[ny][nx]:
                            return None, set()
                    elif (nx, ny) not in visited:
                        stack.append((nx, ny))
        return owner if owner is not None else "", visited

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result = {"B": set(), "W": set(), "": set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                owner, territory = self.territory(x, y)
                if territory:
                    result[owner].update(territory)
        return result
