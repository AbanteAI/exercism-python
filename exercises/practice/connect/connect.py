
class ConnectGame:
        self.board = [list(row) for row in board.split("\n")]
        self.board = board

    def get_winner(self):
        # Check for a winning connection
        def dfs(i, j, player):
            if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]) or self.board[i][j] != player:
                return False
            if (player == "O" and j == len(self.board[0]) - 1) or (player == "X" and i == len(self.board) - 1):
                return True
            self.board[i][j] = "#"
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]
            for dx, dy in directions:
                if dfs(i + dx, j + dy, player):
                    return True
            self.board[i][j] = player
            return False

        # Check for winner
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O" and dfs(i, j, "O"):
                    return "O"
                if self.board[i][j] == "X" and dfs(i, j, "X"):
                    return "X"
        return ""
