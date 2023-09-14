
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
        owner = self.board[y][x]
        if owner in ('W', 'B'):
            return owner, set()

        visited = set()
        stack = [(x, y)]
        territories = set()

        while stack:
            cx, cy = stack.pop()
            visited.add((cx, cy))
            territories.add((cx, cy))

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = cx + dx, cy + dy

                if (0 <= nx < len(self.board[0]) and
                        0 <= ny < len(self.board) and
                        (nx, ny) not in visited):

                    neighbor = self.board[ny][nx]
                    if neighbor == owner:
                        stack.append((nx, ny))
                    elif neighbor in ('W', 'B'):
                        owner = neighbor

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
        result = {'W': set(), 'B': set(), '': set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if (x, y) not in (result['W'] | result['B'] | result['']):
                    owner, territories = self.territory(x, y)
                    result[owner].update(territories)
        return result
