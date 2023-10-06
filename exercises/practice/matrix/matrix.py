class Matrix:
        rows = matrix_string.split("\n")
        self.matrix = [[int(num) for num in row.split()] for row in rows]

        def row(self, index):
            return self.matrix[index - 1]
        def column(self, index):
            return [row[index - 1] for row in self.matrix]