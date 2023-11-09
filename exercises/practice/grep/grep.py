import re

def grep(pattern, flags, files):
    # Compile the pattern with the appropriate flags
    re_flags = 0
    if '-i' in flags:
        re_flags |= re.IGNORECASE
    compiled_pattern = re.compile(pattern, re_flags)

    # Function to determine if a line matches the pattern
    def is_match(line):
        if '-x' in flags:
            return compiled_pattern.fullmatch(line) is not None
        else:
            return compiled_pattern.search(line) is not None

    # Invert the match function if the -v flag is present
    if '-v' in flags:
        original_is_match = is_match
        is_match = lambda line: not original_is_match(line)

    # Prepare the results list
    results = []

    # Process each file
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        # Check if we only need to output the file names with -l flag
        # Check if we only need to output the file names with -l flag
        if '-l' in flags:
            if any(is_match(line) for line in lines):
                results.append(file + '\n')
            continue

        # Otherwise, process each line
        for i, line in enumerate(lines, 1):
            if is_match(line.strip()):
                # Build the output string
                output = ''
                if len(files) > 1:
                    output += f'{file}:'
                if '-n' in flags and '-l' not in flags:
                    output += f'{i}:'
                output += line
                results.append(output)

    return ''.join(results)