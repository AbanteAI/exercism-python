import re

def grep(pattern, flags, files):
    result = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.rstrip('\n')
                if 'n' in flags:
                    line = f"{i+1}:{line}"
                if 'i' in flags:
                if 'i' in flags:
                    compiled_pattern = re.compile(pattern, re.IGNORECASE)
                if 'x' in flags:
                    compiled_pattern = re.compile(f"^{pattern}$")
                if re.search(compiled_pattern, line) and ('v' not in flags or 'v' in flags and 'l' in flags):
                if re.search(pattern, line) and ('v' not in flags or 'v' in flags and 'l' in flags):
                    if 'l' in flags:
                        result.append(file)
                        break
                    else:
                        result.append(f"{file}:{line}")
                elif 'v' in flags and 'l' not in flags:
                    result.append(f"{file}:{line}")
    return result
