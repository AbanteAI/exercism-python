import re
def grep(pattern, flags, files):
    results = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            if '-x' in flags:
                if re.fullmatch(pattern, line, re.I if '-i' in flags else 0):
                    results.append(f"{file}:{i}:{line}" if '-n' in flags else f"{file}:{line}")
            else:
                if re.search(pattern, line, re.I if '-i' in flags else 0):
                    results.append(f"{file}:{i}:{line}" if '-n' in flags else f"{file}:{line}")
    
    if '-l' in flags:
        return '' if not results else [file for file, _, _ in results]
    if '-v' in flags:
        return '' if not results else [line for _, _, line in results]
    
    return '' if not results else [line for _, line in results]