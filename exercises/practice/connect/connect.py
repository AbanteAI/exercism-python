
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row.strip()) for row in board.splitlines()]
        self.board_height = len(self.board)
        self.board_width = len(self.board[0]) if self.board else 0

    def get_winner(self):
        # Check for winner 'O' (top to bottom)
        for x in range(self.board_width):
            if self.board[0][x] == 'O' and self._search(x, 0, 'O', set()):
                return 'O'
        # Check for winner 'X' (left to right)
        for y in range(self.board_height):
            if self.board[y][0] == 'X' and self._search(0, y, 'X', set()):
                return 'X'
        return ""

    def _search(self, x, y, player, visited):
        if (player == 'O' and y == self.board_height - 1) or (player == 'X' and x == self.board_width - 1):
            return True
        visited.add((x, y))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.board_width and 0 <= ny < self.board_height and
                    self.board[ny][nx] == player and (nx, ny) not in visited):
                if self._search(nx, ny, player, visited):
                    return True
        return False
