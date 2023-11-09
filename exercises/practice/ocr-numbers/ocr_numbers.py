def convert(input_grid):
    # Define the OCR representation of each number
    ocr_numbers = {
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

    # Check for correct input size
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    # Process each 3x4 block of the input grid
    result = []
    for row_block in range(0, len(input_grid), 4):
        # Initialize the string for the current line of numbers
        current_line = ""
        for col_block in range(0, len(input_grid[row_block]), 3):
            # Extract the 3x4 block and convert it to a string
            ocr_block = "".join(input_grid[row_block + row][col_block:col_block + 3] for row in range(4))
            # Convert the block to the corresponding number or '?'
            current_line += ocr_numbers.get(ocr_block, "?")
        result.append(current_line)

    # Join the lines with commas and return the result
    return ",".join(result)

