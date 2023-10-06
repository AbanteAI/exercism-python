
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row.strip()) for row in board.splitlines()]

    def get_winner(self):
    def get_winner(self):
        def search(player, pos, visited):
            if player == 'X' and pos[1] == len(self.board[0]) - 1:
                return True
            if player == 'O' and pos[0] == len(self.board) - 1:
                return True

            visited.add(pos)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)):
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]) and self.board[nx][ny] == player and (nx, ny) not in visited:
                    if search(player, (nx, ny), visited):
                        return True
            return False

        for i, cell in enumerate(self.board[0]):
            if cell == 'X' and search('X', (0, i), set()):
                return 'X'

        for i, row in enumerate(self.board):
            if row[0] == 'O' and search('O', (i, 0), set()):
                return 'O'

        return ""

