import re


def grep(pattern, flags, files):
    results = []

    # Apply flags
    if '-i' in flags:
        pattern = pattern.lower()

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        for index, line in enumerate(lines):
            line_to_match = line.strip()
            if '-i' in flags:
                line_to_match = line_to_match.lower()

            # Check for matches
            if '-x' in flags:
                match = pattern == line_to_match
            else:
                match = pattern in line_to_match

            if '-v' in flags:
                match = not match

            if match:
                if '-l' in flags:
                    results.append(file)
                    break
                elif '-n' in flags:
                    results.append(f"{file}:{index + 1 + 1}:{line.strip()}")
                else:
                    results.append(f"{file}:{line.strip()}")

    return '\n'.join(results)