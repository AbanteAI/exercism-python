
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
        self.max_x = len(board[0])
        self.max_y = len(board)

    def territory(self, x, y):
        if not (0 <= x < self.max_x and 0 <= y < self.max_y):
            raise ValueError('Invalid coordinate')
        # Implementation of territory method will go here

    def territories(self):
        # Implementation of territories method will go here
        pass
