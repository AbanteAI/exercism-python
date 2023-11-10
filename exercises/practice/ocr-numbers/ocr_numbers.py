def convert(input_grid):
    # Define the patterns for each digit
    digit_patterns = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9",
    }

    # Check for correct input size
    if len(input_grid) % 4 != 0 or any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input lines is not a multiple of four or number of input columns is not a multiple of three")

    # Split the input grid into 3x4 chunks for each digit
    rows_per_digit = 4
    cols_per_digit = 3
    num_digits = len(input_grid[0]) // cols_per_digit
    digits = [''.join(input_grid[row][col:col+cols_per_digit] for row in range(r, r+rows_per_digit)) for r in range(0, len(input_grid), rows_per_digit) for col in range(0, len(input_grid[0]), cols_per_digit)]

    # Convert each chunk to its corresponding number
    result = [digit_patterns.get(digit, '?') for digit in digits]

    # Group the results by line
    line_length = len(input_grid[0]) // cols_per_digit
    lines = ["".join(result[i:i+line_length]) for i in range(0, len(result), line_length)]

    return ",".join(lines)