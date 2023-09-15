def convert(input_grid):
    # Step One: Convert a simple binary font to a string containing 0 or 1
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
    
    # Step Two: Recognize multi-character binary strings and replace garbled numbers with '?'
    if len(input_grid) % 4 != 0 or any(len(row) % 3 != 0 for row in input_grid):
        return "?"
    
    result = ""
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[i]), 3):
            binary_string = ""
            for k in range(4):
                binary_string += input_grid[i+k][j:j+3]
            result += binary_font.get(binary_string, "?")
        result += ","
    
    return result.rstrip(",")

# Step Three: Recognize all numbers 0 through 9, both individually and as part of a larger string

# Step Four: Handle multiple numbers, one per line, and join the lines with commas

