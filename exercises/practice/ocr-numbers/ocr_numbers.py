def convert(input_grid):
    binary_font = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9"
    }

    if len(input_grid) % 4 != 0 or any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = ""
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[i]), 3):
            digit = ""
            for k in range(4):
                digit += input_grid[i + k][j:j + 3]
            result += binary_font.get(digit, "?")
        if i + 4 < len(input_grid):
            result += ","
        raise ValueError("Number of input lines is not a multiple of four")

