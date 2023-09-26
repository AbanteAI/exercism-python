class Queen:
        self.row = row
        self.column = column
        pass

    def can_attack(self, another_queen):
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        row_diff = abs(self.row - another_queen.row)
        col_diff = abs(self.column - another_queen.column)
        return row_diff == col_diff
            return True
        row_diff = abs(self.row - another_queen.row)
        col_diff = abs(self.column - another_queen.column)
        return row_diff == col_diff
