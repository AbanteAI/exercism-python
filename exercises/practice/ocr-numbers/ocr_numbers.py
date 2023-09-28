def convert(input_grid):
    rows = len(input_grid)
    if rows % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    columns = len(input_grid[0])
    if columns % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    
    result = ""
    for i in range(0, rows, 4):
        for j in range(0, columns, 3):
            number = input_grid[i:i+4]
            digit = ""
            for k in range(4):
                digit += number[k][j:j+3]
            result += get_digit(digit)
        result += ","
    
    return result.rstrip(",")


def get_digit(digit):
    digits = {
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
    return digits.get(digit, "?")