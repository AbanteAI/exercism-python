
class Board:
WHITE = 'W'
BLACK = 'B'
NONE = ''
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
        owner, territory = self._find_territory(x, y)
        return (owner, territory)

    def territories(self):
        territories = {BLACK: set(), WHITE: set(), NONE: set()}
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.board[y][x] == ' ':
                    owner, territory = self._find_territory(x, y)
                    if territory:
                        territories[owner].update(territory)
        return territories
        return territories

    def _find_territory(self, x, y):
        if self.board[y][x] != ' ':
            return None, set()
        visited = set()
        stack = [(x, y)]
        owner = None
        while stack:
            current_x, current_y = stack.pop()
            if (current_x, current_y) in visited:
                continue
            visited.add((current_x, current_y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = current_x + dx, current_y + dy
                if not (0 <= next_x < self.max_x and 0 <= next_y < self.max_y):
                    continue
                next_pos = self.board[next_y][next_x]
                elif next_pos in [BLACK, WHITE]:
                    if owner is None:
                        owner = next_pos
                    elif owner != next_pos:
                        return NONE, set()
        return owner if owner else NONE, visited
        return owner if owner else '', visited
