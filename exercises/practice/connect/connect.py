
class ConnectGame:
    def __init__(self, board):
    def __init__(self, board):
        self.board = board

    def get_winner(self):
        size = len(self.board)
        connected = set()

        def dfs(row, col, player):
            if row < 0 or row >= size or col < 0 or col >= size:
                return False
            if self.board[row][col] != player or (row, col) in connected:
                return False
            if player == "O" and col == size - 1:
                return True
            if player == "X" and row == 0:
                return True

            connected.add((row, col))
            for dr, dc in [(1, 0), (-1, 1), (0, 1), (1, -1), (-1, 0), (0, -1)]:
                if dfs(row + dr, col + dc, player):
                    return True
            connected.remove((row, col))
            return False

        for col in range(size):
            if self.board[0][col] == "X":
                if dfs(0, col, "X"):
                    return "X"
        for row in range(size):
            if self.board[row][0] == "O":
                if dfs(row, 0, "O"):
                    return "O"
        return ""