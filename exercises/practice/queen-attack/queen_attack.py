class Queen:
    def __init__(self, row, column):
        if not (0 <= row < 8) or not (0 <= column < 8):
        if not (0 <= row < 8):
            raise ValueError("row not on board")
        if not (0 <= column < 8):
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        if not isinstance(another_queen, Queen):
            raise ValueError("Invalid queen object")
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (
            self.row == another_queen.row
            or self.column == another_queen.column
            or abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
        )
