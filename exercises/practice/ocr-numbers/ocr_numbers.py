OCR_NUMBERS = {
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

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    def parse_ocr_digit(ocr_digit):
        return OCR_NUMBERS.get(ocr_digit, "?")

    def chunk_string(string, size):
        return [string[i:i+size] for i in range(0, len(string), size)]

    # Split the input grid into 4-row chunks for each number
    chunks = [input_grid[i:i + 4] for i in range(0, len(input_grid), 4)]
    converted_numbers = []

    for chunk in chunks:
        # Transpose the chunk to group by digit
        transposed_chunk = [''.join(chunk) for chunk in zip(*[chunk_string(row, 3) for row in chunk])]
        # Parse each OCR digit and concatenate to form the number
        number = ''.join(parse_ocr_digit(''.join(transposed_chunk[i:i + 4])) for i in range(0, len(transposed_chunk), 4))
        converted_numbers.append(number)

    return ','.join(converted_numbers)

