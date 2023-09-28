def is_valid_grid(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

def convert_single(pattern):
    OCR_MAP = {
        " _ | ||_|": "0",
        "     |  |": "1",
        " _  _||_ ": "2",
        " _  _| _|": "3",
        "   |_|  |": "4",
        " _ |_  _|": "5",
        " _ |_ |_|": "6",
        " _   |  |": "7",
        " _ |_||_|": "8",
        " _ |_| _|": "9"
    }
    return OCR_MAP.get(pattern, "?")

def convert(input_grid):
    is_valid_grid(input_grid)

    result = []
    for i in range(0, len(input_grid), 4):
        row_result = []
        for j in range(0, len(input_grid[i]), 3):
            pattern = input_grid[i][j:j + 3] + input_grid[i + 1][j:j + 3] + input_grid[i + 2][j:j + 3]
            row_result.append(convert_single(pattern))
        result.append("".join(row_result))

    return ",".join(result)