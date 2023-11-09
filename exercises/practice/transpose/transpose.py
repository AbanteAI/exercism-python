def transpose(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')
    
    # If input is empty, return an empty list
    if not lines or all(line == '' for line in lines):
        return []
    
    # Find the length of the longest string
    max_length = max(len(line) for line in lines)
    
    # Pad the lines with spaces to the left to make them all the same length
    padded_lines = [line.ljust(max_length) for line in lines]
    
    # Transpose the lines by zipping the padded lines, which creates tuples of characters at the same index
    transposed_lines = list(map(list, zip(*padded_lines)))
    
    # Convert the lists of characters back into strings, strip trailing spaces, and return
    return [''.join(line).rstrip() for line in transposed_lines]
