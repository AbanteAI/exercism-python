from typing import List

class ConnectGame:
    def __init__(self, board: str):
        self.board = [list(row.strip()) for row in board.splitlines()]
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def get_winner(self) -> str:
        def dfs(x: int, y: int, player: str, visited: List[List[bool]]) -> bool:
            if player == "X" and x == self.rows - 1:
                return True
            if player == "O" and y == self.cols - 1:
                return True

            visited[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and not visited[nx][ny] and self.board[nx][ny] == player:
                    if dfs(nx, ny, player, visited):
                        return True

            return False

        for player in ["X", "O"]:
            visited = [[False] * self.cols for _ in range(self.rows)]
            if player == "X":
                for y in range(self.cols):
                    if self.board[0][y] == "X" and dfs(0, y, "X", visited):
                        return "X"
            else:
                for x in range(self.rows):
                    if self.board[x][0] == "O" and dfs(x, 0, "O", visited):
                        return "O"

        return ""
