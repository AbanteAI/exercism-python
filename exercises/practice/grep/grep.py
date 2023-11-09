import re

def grep(pattern, flags, files):
    flags = flags.split()
    case_insensitive = '-i' in flags
    line_numbers = '-n' in flags
    file_names_only = '-l' in flags
    invert_match = '-v' in flags
    match_whole_line = '-x' in flags
    results = []

for file in files:
    with open(file, 'r') as f:
        for line_number, content in enumerate(f, 1):
            content = content.rstrip()  # remove trailing newline
            if case_insensitive:
                pattern = re.compile(pattern, re.IGNORECASE)
            match = pattern.fullmatch(content) if match_whole_line else pattern.search(content)
            if (match and not invert_match) or (not match and invert_match):
                if file_names_only:
                    results.append(file)
                    break
                else:
                    line_format = f"{file}:" if len(files) > 1 else ""
                    if line_numbers:
                        line_format += f"{line_number}:"
                    line_format += content
                    results.append(line_format)
    if file_names_only and file in results:
        break

if file_names_only:
    results = list(set(results))  # Remove duplicates

return '\n'.join(results)