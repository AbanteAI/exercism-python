def convert(input_grid):
    # Validate input grid dimensions
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    # OCR representation to number mapping
    ocr_to_num = {
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

    # Parse input grid into OCR representations
    rows_per_digit = 4
    cols_per_digit = 3
    ocr_representations = [
        ''.join(input_grid[row][col:col + cols_per_digit] for row in range(j, j + rows_per_digit))
        for j in range(0, len(input_grid), rows_per_digit)
        for col in range(0, len(input_grid[j]), cols_per_digit)
    ]

    # Convert OCR representations to numbers
    numbers = [ocr_to_num.get(rep.replace('\n', ''), '?') for rep in ocr_representations]

    # Group numbers by line and join them with commas
    num_digits_per_line = len(input_grid[0]) // cols_per_digit
    lines_of_numbers = [
        ''.join(numbers[i:i + num_digits_per_line])
        for i in range(0, len(numbers), num_digits_per_line)
    ]

    return ','.join(lines_of_numbers)

