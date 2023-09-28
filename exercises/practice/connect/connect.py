
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row) for row in board]

    def has_won(self, player):
        visited = set()
        stack = []

        if player == 'O':
            stack = [(0, i) for i, cell in enumerate(self.board[0]) if cell == player]
        elif player == 'X':
            stack = [(i, 0) for i, row in enumerate(self.board) for cell in row if cell == player]

        while stack:
            x, y = stack.pop()
            if player == 'O' and x == len(self.board) - 1 and (x, y) not in visited:
                return True
            if player == 'X' and y == len(self.board[0]) - 1 and (x, y) not in visited:
                return True

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]) and (nx, ny) not in visited and self.board[nx][ny] == player:
                    visited.add((nx, ny))
                    stack.append((nx, ny))

        return False

    def get_winner(self):
        if self.has_won('O'):
            return 'O'
        elif self.has_won('X'):
            return 'X'
        else:
            return ''
