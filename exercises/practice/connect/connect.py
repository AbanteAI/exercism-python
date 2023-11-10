
class ConnectGame:
    def __init__(self, board):
        self.board = board.splitlines()
        self.board_height = len(self.board)
        self.board_width = len(self.board[0])
        self.visited = set()

    def get_winner(self):
        for x in range(self.board_width):
            if self.board[0][x] == 'O' and self.dfs(0, x, 'O'):
                return 'O'
        for y in range(self.board_height):
            if self.board[y][0] == 'X' and self.dfs(y, 0, 'X'):
                return 'X'
        return ""

    def dfs(self, y, x, player):
        if player == 'O' and y == self.board_height - 1:
            return True
        if player == 'X' and x == self.board_width - 1:
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]
        self.visited.add((y, x))
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < self.board_height and
                0 <= nx < self.board_width and
                self.board[ny][nx] == player and
                (ny, nx) not in self.visited and
                self.dfs(ny, nx, player)):
                    return True
        return False
