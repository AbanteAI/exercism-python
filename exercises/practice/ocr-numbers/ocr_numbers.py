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

    if len(input_grid) % 4 != 0 or any(len(line) % 3 != 0 for line in input_grid):
        return "Error: Invalid input size"

    result = []
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[i]), 3):
            digit = "".join(input_grid[i + k][j:j + 3] for k in range(3))
            result.append(binary_font.get(digit, "?"))
    return "".join(result)