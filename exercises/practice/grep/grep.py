import re

def grep(pattern, flags, files):
    case_insensitive = '-i' in flags
    line_numbers = '-n' in flags
    file_names_only = '-l' in flags
    invert_match = '-v' in flags
    match_entire_line = '-x' in flags
    matching_lines = []

    compiled_pattern = re.compile(pattern, re.IGNORECASE) if case_insensitive else re.compile(pattern)

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines, start=1):
            line = line.rstrip('\n')
            match = compiled_pattern.fullmatch(line) if match_entire_line else compiled_pattern.search(line)
            if (match and not invert_match) or (not match and invert_match):
                prefix = f"{file}:" if len(files) > 1 else ""
                prefix += f"{i}:" if line_numbers else ""
                if file_names_only:
                    matching_lines.append(file)
                    break
                else:
                    matching_lines.append(f"{prefix}{line}")

    return "\n".join(matching_lines)