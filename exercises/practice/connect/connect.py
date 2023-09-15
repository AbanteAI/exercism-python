
class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0])

    def get_winner(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == 'X' and col == 0:
                    if self._is_winning_connection('X', set(), row, col):
                        return 'X'
                if self.board[row][col] == 'O' and row == 0:
                    if self._is_winning_connection('O', set(), row, col):
                        return 'O'
        return ''
    def _is_winning_connection(self, player, visited, row, col):
    def _is_winning_connection(self, player, visited, row, col):
        if player == 'X' and (col == self.width - 1 or row == self.height - 1):
            return True
        if player == 'O' and (row == self.height - 1 or col == self.width - 1):
            return True

        visited.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (
                0 <= new_row < self.height
                and 0 <= new_col < self.width
                and self.board[new_row][new_col] == player
                and (new_row, new_col) not in visited
                and self._is_winning_connection(player, visited, new_row, new_col)
            ):
                return True

        return False
