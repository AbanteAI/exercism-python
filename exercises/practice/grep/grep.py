import re

def grep(pattern, flags, files):
    case_insensitive = '-i' in flags
    line_numbers = '-n' in flags
    file_names_only = '-l' in flags
    invert_match = '-v' in flags
    match_whole_line = '-x' in flags

    compiled_pattern = re.compile(pattern, re.IGNORECASE) if case_insensitive else re.compile(pattern)
    matching_lines = []

    for file in files:
        with open(file, 'r') as f:
            for line_number, line in enumerate(f, start=1):
                line = line.rstrip('\n')
                match = compiled_pattern.fullmatch(line) if match_whole_line else compiled_pattern.search(line)
                if match is not None if not invert_match else match is None:
                if (match and not invert_match) or (not match and invert_match):
                    if file_names_only:
                        matching_lines.append(file)
                        break
                    prefix = f"{file}:" if len(files) > 1 else ""
                    prefix += f"{line_number}:" if line_numbers else ""
                    matching_lines.append(f"{prefix}{line}")

    return '\n'.join(matching_lines) + ('\n' if matching_lines else '')