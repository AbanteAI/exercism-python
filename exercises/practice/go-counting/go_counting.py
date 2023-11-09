
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
        if not (0 <= x < len(self.board[0]) and 0 <= y < len(self.board)):
            raise ValueError('Invalid coordinate')

        # Implementation of territory method will go here
        # Placeholder for the actual logic
        owner = ""
        territories = set()
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
        # Implementation of territories method will go here
        # Placeholder for the actual logic
        territories_dict = {"W": set(), "B": set(), "": set()}
        return territories_dict
