class Queen:
    def __init__(self, row, column):
        if not (0 <= row <= 7):
            raise ValueError("row not on board")
        if not (0 <= column <= 7):
            raise ValueError("column not on board")
        self.row = row
        self.column = column
        if not (0 <= column <= 7):
            raise ValueError("column not positive")
        self.row = row
        self.column = column
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Queens cannot occupy the same position")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False
