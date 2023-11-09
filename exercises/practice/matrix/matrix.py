class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(num) for num in line.split()] for line in matrix_string.splitlines()]
        self.columns = [list(col) for col in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
