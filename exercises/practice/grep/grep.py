import re

    results = []
    results = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.rstrip('\n')
                if '-n' in flags:
                    line = f'{i+1}:{line}'
                match = re.search(pattern, line, re.IGNORECASE if '-i' in flags else 0)
                if match and ('-x' not in flags or match.group() == line):
                    results.append(f'{file}:{line}')
                elif '-v' in flags and not match:
                    results.append(f'{file}:{line}')
    return '\n'.join(results) if results else ""