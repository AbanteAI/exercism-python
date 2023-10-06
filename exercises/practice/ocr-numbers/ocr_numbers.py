def convert(input_grid):
    # Define the mapping of OCR numbers
    ocr_mapping = {
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

    # Split the input grid into rows
    rows = input_grid.split("\n")

    # Check for valid row count
    if len(rows) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Check for valid column count
    if any(len(row) % 3 != 0 for row in rows):
        raise ValueError("Number of input columns is not a multiple of three")

    # Convert each group of rows into OCR numbers
    result = []
    for i in range(0, len(rows), 4):
        for j in range(0, len(rows[i]), 3):
            ocr_number = "".join(rows[i+k][j:j+3] for k in range(3))
            result.append(ocr_mapping.get(ocr_number, "?"))

    return ",".join(result) if all(num != "?" for num in result) else "?"

