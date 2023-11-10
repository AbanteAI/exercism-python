WHITE = "W"
BLACK = "B"
NONE = ""
# The above constants represent the state of a point on the Go board.
# 'WHITE' for a point occupied by a white stone, 'BLACK' for a black stone,
# and 'NONE' for an empty point.

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.board_height = len(board)
        self.board_width = len(board[0]) if board else 0

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
        if not (0 <= x < self.board_width and 0 <= y < self.board_height):
            raise ValueError('Invalid coordinate')

        # Implementation of territory method
        # Placeholder for actual logic to determine the owner and territories
        owner = ""
        territories = set()
        # TODO: Implement the logic to determine the owner and territories

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
        # Implementation of territories method
        # Placeholder for actual logic to find owners and territories
        territories_info = {"W": set(), "B": set(), "": set()}
        # TODO: Implement the logic to find owners and territories

        return territories_info
