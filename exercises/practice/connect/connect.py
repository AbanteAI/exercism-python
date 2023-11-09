
class ConnectGame:
    def __init__(self, board):
        self.board = board.strip().splitlines()
        self.board_height = len(self.board)
        self.board_width = len(self.board[0]) if self.board else 0
        self.visited = set()

    def get_winner(self):
        # Check for a winning path for each player
        for player in ('X', 'O'):
            if self._has_winning_path(player):
                return player
        return ""

    def _has_winning_path(self, player):
        # Starting positions for 'X' and 'O'
        start_positions = {
            'X': [(0, i) for i in range(self.board_width) if self.board[0][i] == 'X'],
            'O': [(i, 0) for i in range(self.board_height) if self.board[i][0] == 'O']
        }

        # DFS to find a path from one side to the other
        def dfs(row, col):
            if (row, col) in self.visited:
                return False
            self.visited.add((row, col))
            # Check if the current position is on the opposite side
            if player == 'X' and row == self.board_height - 1:
                return True
            if player == 'O' and col == self.board_width - 1:
                return True
            # Explore neighbors
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.board_height and 0 <= new_col < self.board_width and self.board[new_row][new_col] == player:
                    if dfs(new_row, new_col):
                        return True
            return False

        # Check each starting position for a path to the opposite side
        for row, col in start_positions[player]:
            self.visited.clear()
            if dfs(row, col):
                return True
        return False
        return False
