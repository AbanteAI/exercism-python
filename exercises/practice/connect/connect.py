
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row.strip()) for row in board.splitlines()]
        self.height = len(self.board)
        self.width = len(self.board[0]) if self.height > 0 else 0

    def get_winner(self):
        # Check for winner 'O' (top to bottom)
        for col in range(self.width):
            if self.board[0][col] == 'O' and self.search(0, col, 'O', set()):
                return 'O'
        # Check for winner 'X' (left to right)
        for row in range(self.height):
            if self.board[row][0] == 'X' and self.search(row, 0, 'X', set()):
                return 'X'
        return ""

    def search(self, row, col, player, visited):
        if player == 'O' and row == self.height - 1:
            return True
        if player == 'X' and col == self.width - 1:
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]
        visited.add((row, col))
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (0 <= r < self.height and 0 <= c < self.width and
                    (r, c) not in visited and self.board[r][c] == player):
                if self.search(r, c, player, visited):
                    return True
        return False
