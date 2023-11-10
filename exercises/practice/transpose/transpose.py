def transpose(input_lines):
    # Split the input text into lines
    lines = input_lines.split('\n')
    # Transpose the lines
    transposed = list(map(list, zip(*map(lambda x: list(x.ljust(len(max(lines, key=len)))), lines))))
    # Convert list of lists back to list of strings and strip trailing spaces
    transposed_lines = [''.join(line).rstrip() for line in transposed]
    # Join the transposed lines into a single string with newlines
    return '\n'.join(transposed_lines)