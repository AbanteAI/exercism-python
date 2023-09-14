def convert(input_grid):
    OCR_MAP = {
        " _ | ||_|": "0",
        "     |  |": "1",
        " _  _| _|": "2",
        " _  _| _|": "3",
        "   |_|  |": "4",
        " _ |_  _|": "5",
        " _ |_ |_|": "6",
        " _   |  |": "7",
        " _ |_||_|": "8",
        " _ |_| _|": "9",
    }

    if len(input_grid) % 4 != 0 or any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Invalid grid size")

    result = ""
    for row_start in range(0, len(input_grid), 4):
        for col_start in range(0, len(input_grid[row_start]), 3):
            ocr_digit = ""
            for row in input_grid[row_start : row_start + 3]:
                ocr_digit += row[col_start : col_start + 3]
            result += OCR_MAP.get(ocr_digit, "?")
        if row_start + 4 < len(input_grid):
            result += ","
    return result