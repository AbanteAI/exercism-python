
class ConnectGame:
    def __init__(self, board):
        pass
        self.board = [list(row.strip()) for row in board.splitlines()]

    def _is_winner(self, player):
        visited = set()
        stack = []

        if player == "X":
            stack = [(0, i) for i, cell in enumerate(self.board[0]) if cell == player]
        elif player == "O":
            stack = [(i, 0) for i, row in enumerate(self.board) if row[0] == player]

        while stack:
            x, y = stack.pop()
            if (player == "X" and y == len(self.board[-1]) - 1) or (player == "O" and x == len(self.board) - 1):
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(self.board)
                    and 0 <= ny < len(self.board[nx])
                    and self.board[nx][ny] == player
                    and (nx, ny) not in visited
                ):
                    visited.add((nx, ny))
                    stack.append((nx, ny))

        return False
    def get_winner(self):
    def get_winner(self):
        if self._is_winner("X"):
            return "X"
        elif self._is_winner("O"):
            return "O"
        else:
            return ""
