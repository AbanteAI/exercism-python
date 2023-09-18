def convert(input_grid):
    pass


def recognize_digit(ocr_digit):
    ocr_digits = {
        " _ | ||_|": "0",
        "     |  |": "1",
        " _  _| _|": "2",
        " _  _| _|": "3",
        "   |_|  |": "4",
        " _ |_  _|": "5",
        " _ |_ |_|": "6",
        " _   |  |": "7",
        " _ |_||_|": "8",
        " _ |_| _|": "9"
    }
    ocr_digit_str = ''.join(ocr_digit)
    return ocr_digits.get(ocr_digit_str, '?')

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = []
    for i in range(0, len(input_grid), 4):
        line_result = []
        for j in range(0, len(input_grid[i]), 3):
            ocr_digit = [
                input_grid[i][j:j+3],
                input_grid[i+1][j:j+3],
                input_grid[i+2][j:j+3]
            ]
            line_result.append(recognize_digit(ocr_digit))
        result.append(''.join(line_result))
    return ','.join(result)