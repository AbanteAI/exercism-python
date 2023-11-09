
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row.strip()) for row in board.splitlines()]
        self.height = len(self.board)
        self.width = len(self.board[0]) if self.height > 0 else 0

    def get_winner(self):
        # Helper function to perform DFS
        def dfs(player, x, y, visited):
            if not (0 <= x < self.width and 0 <= y < self.height) or self.board[y][x] != player or (x, y) in visited:
                return False
            if (player == 'O' and y == self.height - 1) or (player == 'X' and x == self.width - 1):
                return True
            visited.add((x, y))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
            return any(dfs(player, x + dx, y + dy, visited) for dx, dy in directions)

        # Check for a winning path for each player
        for player in ('O', 'X'):
            starting_positions = [(0, y) for y in range(self.height)] if player == 'X' else [(x, 0) for x in range(self.width)]
            if any(dfs(player, x, y, set()) for x, y in starting_positions):
                return player
        return ''
