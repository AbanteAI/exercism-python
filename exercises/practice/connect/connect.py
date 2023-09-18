
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row) for row in board]

    def get_winner(self):
        if self.has_won("X"):
            return "X"
        elif self.has_won("O"):
            return "O"
        else:
            return ""

    def has_won(self, player):
        start_points, end_points = self.get_points(player)

        if not start_points or not end_points:
            return False

        visited = set()
        for start_point in start_points:
            if self.dfs(start_point, end_points, visited, player):
                return True
        return False

    def dfs(self, current, end_points, visited, player):
        if current in end_points:
            return True

        visited.add(current)
        for neighbor in self.get_neighbors(current):
            if neighbor not in visited and self.board[neighbor[0]][neighbor[1]] == player:
                if self.dfs(neighbor, end_points, visited, player):
                    return True
        return False

    def get_points(self, player):
        if player == "X":
            start_points = [(i, 0) for i in range(len(self.board)) if self.board[i][0] == player]
            end_points = [(i, len(self.board[0]) - 1) for i in range(len(self.board)) if self.board[i][-1] == player]
        else:
            start_points = [(0, i) for i in range(len(self.board[0])) if self.board[0][i] == player]
            end_points = [(len(self.board) - 1, i) for i in range(len(self.board[-1])) if self.board[-1][i] == player]

        return start_points, end_points

        return start_points, end_points

    def get_neighbors(self, point):
        x, y = point
        neighbors = [
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
        ]
        if x % 2 == 0:
            neighbors.remove((x + 1, y - 1))
            neighbors.remove((x - 1, y + 1))
        else:
            neighbors.remove((x + 1, y))
            neighbors.remove((x - 1, y))
        return [(x, y) for x, y in neighbors if 0 <= x < len(self.board) and 0 <= y < len(self.board[0])]
        return [(x, y) for x, y in neighbors if 0 <= x < len(self.board) and 0 <= y < len(self.board[0])]