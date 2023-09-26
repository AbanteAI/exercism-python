
class ConnectGame:
        self.board = [list(row) for row in board.split('\n')]
        pass

    def get_winner(self):
        board = self.board
        size = len(board)
        visited = set()

        def dfs(row, col, player):
            if row < 0 or row >= size or col < 0 or col >= size or board[row][col] != player or (row, col) in visited:
                return False
            if player == 'O' and col == size - 1:
                return True
            if player == 'X' and row == size - 1:
                return True

            visited.add((row, col))
            directions = [(0, 1), (0, -1), (-1, 1), (-1, 0), (1, -1), (1, 0)]
            for dx, dy in directions:
                if dfs(row + dx, col + dy, player):
                    return True

            return False

        for i in range(size):
            if dfs(i, 0, 'O'):
                return 'O'
        for j in range(size):
            if dfs(0, j, 'X'):
                return 'X'

        return ''