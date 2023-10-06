class Queen:
    def __init__(self, row, column):
        if not (0 <= row < 8) or not (0 <= column < 8):
        if not (0 <= row < 8):
            raise ValueError("row not on board")
        if not (0 <= column < 8):
            raise ValueError("column not on board")