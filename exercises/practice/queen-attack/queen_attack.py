class Queen:
    def __init__(self, row, column):
        if not (0 <= row < 8) or not (0 <= column < 8):
            raise ValueError("Invalid queen position: row or column not on board")
            raise ValueError("Invalid queen position")
        self.row = row
        self.column = column
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if not isinstance(another_queen, Queen):
        if not isinstance(another_queen, Queen):
            raise ValueError("Invalid queen object: not an instance of Queen class")
        
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        
        row_diff = abs(self.row - another_queen.row)
        col_diff = abs(self.column - another_queen.column)
        return row_diff == col_diff
        pass
