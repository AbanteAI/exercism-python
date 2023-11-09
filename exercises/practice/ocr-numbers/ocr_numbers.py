def convert(input_grid):
    # Define the OCR representations for numbers 0-9
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
        " _ |_| _|   ": "9",
    }

    # Check for correct input size
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    # Process each 3x4 block of the input grid
    result = []
    for i in range(0, len(input_grid), 4):
        digits = []
        for j in range(0, len(input_grid[i]), 3):
            # Extract the 3x4 block representing a single number
            block = "".join(input_grid[i+k][j:j+3] for k in range(4))
            # Convert the block to a number or '?'
            digits.append(ocr_numbers.get(block, '?'))
        # Join the converted numbers and add to the result list
        result.append("".join(digits))

    # Join the results with commas for multiple lines
    return ",".join(result)

