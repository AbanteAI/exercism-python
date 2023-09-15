class Queen:
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False
