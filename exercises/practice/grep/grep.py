import re

def grep(pattern, flags, files):
    result = []
    for file in files:
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if '-n' in flags:
                        line = f'{file}:{i + 1}:{line}'
                    else:
                        line = f'{file}:{line}'
                    if '-i' in flags:
                    if '-i' in flags:
                        compiled_pattern = re.compile(pattern, re.IGNORECASE)
                    if '-x' in flags:
                        compiled_pattern = re.compile(f'^{pattern}$')
                    if '-v' in flags:
                        if not re.search(compiled_pattern, line):
                            result.append(line)
                    else:
                        if re.search(compiled_pattern, line):
                            result.append(line)
                    if '-v' in flags:
                        if not re.search(pattern, line):
                            result.append(line)
                    else:
                        if re.search(pattern, line):
                            result.append(line)
        except FileNotFoundError:
            continue
    return result
