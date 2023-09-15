def convert(input_grid):
    pass
OCR_NUMBERS = {
    " _ | ||_|": "0",
    "     |  |": "1",
    " _  _||_ ": "2",
    " _  _| _|": "3",
    "   |_|  |": "4",
    " _ |_  _|": "5",
    " _ |_ |_|": "6",
    " _   |  |": "7",
    " _ |_||_|": "8",
    " _ |_| _|": "9"
}

def split_numbers(lines):
    if len(lines) % 4 != 0 or any(len(line) % 3 != 0 for line in lines):
        raise ValueError("Invalid input grid size")
    numbers = []
    for row in range(0, len(lines), 4):
        for col in range(0, len(lines[row]), 3):
            number_representation = "".join(lines[row + i][col:col + 3] for i in range(3))
            numbers.append(OCR_NUMBERS.get(number_representation, "?"))
    return numbers

def convert(input_grid):
def convert(input_grid):
    numbers = split_numbers(input_grid)
    return ",".join("".join(numbers[i:i + 9]) for i in range(0, len(numbers), 9))
