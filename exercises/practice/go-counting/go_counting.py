WHITE = "W"
BLACK = "B"
NONE = ""

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
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
        def find_territory(x, y, visited):
            if (x, y) in visited:
                return "", set()
            visited.add((x, y))

            if self.board[y][x] in "BW":
                return self.board[y][x], set()

            owner = ""
            territory = {(x, y)}

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.board[0]) and 0 <= ny < len(self.board):
                    o, t = find_territory(nx, ny, visited)
                    if o == "":
                        territory |= t
                    elif owner == "":
                        owner = o
                    elif owner != o:
                        owner = ""

            return owner, territory

        visited = set()
        return find_territory(x, y, visited)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories = {"B": set(), "W": set(), "": set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if (x, y) not in territories["B"] | territories["W"] | territories[""]:
                    owner, territory = self.territory(x, y)
                    territories[owner] |= territory
        return territories
