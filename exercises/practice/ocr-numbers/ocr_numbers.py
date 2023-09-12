def convert(input_grid):
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
        " _ |_| _|": "9",
    }

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    rows = len(input_grid) // 4
    result = []

    for row in range(rows):
        start = row * 4
        end = start + 4
        row_grid = input_grid[start:end]

        if len(row_grid[0]) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

        cols = len(row_grid[0]) // 3
        row_result = []

        for col in range(cols):
            start = col * 3
            end = start + 3
            pattern = "".join([row_grid[i][start:end] for i in range(4)])
            row_result.append(OCR_MAP.get(pattern, "?"))

        result.append("".join(row_result))

    return ",".join(result)