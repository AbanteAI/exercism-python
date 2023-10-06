
class ConnectGame:
        self.board = [list(row.strip()) for row in board.split('\n')]


    def get_winner(self):
        rows = len(self.board)
        cols = len(self.board[0])
        visited = set()
        directions = [(0, 1), (1, 0), (1, -1)]
        queue = []
        
        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and self.board[row][col] == 'O' and (row, col) not in visited
        
        def bfs(row, col):
            if row == rows - 1:
                return True
            visited.add((row, col))
            queue.append((row, col))
            
            while queue:
                r, c = queue.pop(0)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        if bfs(nr, nc):
                            return True
            return False
        
        for i in range(rows):
            if self.board[i][0] == 'O':
                if bfs(i, 0):
                    return 'O'
        
        return 'X'

