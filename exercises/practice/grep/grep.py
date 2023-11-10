import re

def grep(pattern, flags, files):
    results = []
    case_insensitive = '-i' in flags
    match_entire_line = '-x' in flags
    invert_match = '-v' in flags
    file_names_only = '-l' in flags
    line_numbers = '-n' in flags

    # Compile the pattern for efficiency, considering case insensitivity and full line match
    if match_entire_line:
        pattern = f"^{pattern}$"
    regex_flags = re.IGNORECASE if case_insensitive else 0
    compiled_pattern = re.compile(pattern, regex_flags)

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        for line_number, line in enumerate(lines, start=1):
            match = bool(compiled_pattern.search(line.rstrip('\n')))
            if invert_match:
                match = not match

            if match:
                output_line = line.rstrip('\n')
                if line_numbers:
                    output_line = f"{line_number}:{output_line}"
                if len(files) > 1:
                    output_line = f"{file}:{output_line}"
                results.append(output_line)

    if file_names_only:
        unique_files = set(result.split(':')[0] for result in results)
        return '\n'.join(sorted(unique_files)) + '\n'

    return '\n'.join(results) + '\n' if results else ''