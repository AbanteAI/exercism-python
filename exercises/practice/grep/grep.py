import re

def grep(pattern, flags, files):
    lines = []
    for file in files:
        with open(file, 'r') as f:
            file_lines = f.readlines()
            for i, line in enumerate(file_lines):
                line = line.strip()
                if '-i' in flags:
                    pattern = pattern.lower()
                    line = line.lower()
                if '-x' in flags:
                    if line == pattern:
                        if '-n' in flags:
                            lines.append(f"{file}:{i+1}:{line}")
                        else:
                            lines.append(f"{file}:{line}")
                else:
                    if re.search(pattern, line):
                        if '-n' in flags:
                            lines.append(f"{file}:{i+1}:{line}")
                        else:
                            lines.append(f"{file}:{line}")
    if '-l' in flags:
        matching_files = set()
        for line in lines:
            matching_files.add(line.split(':')[0])
        return list(matching_files)
    elif '-v' in flags:
        matching_lines = []
        for file in files:
            with open(file, 'r') as f:
                file_lines = f.readlines()
                for i, line in enumerate(file_lines):
                    line = line.strip()
                    if '-i' in flags:
                        pattern = pattern.lower()
                        line = line.lower()
                    if '-x' in flags:
                        if line != pattern:
                            if '-n' in flags:
                                matching_lines.append(f"{file}:{i+1}:{line}")
                            else:
                                matching_lines.append(f"{file}:{line}")
                    else:
                        if not re.search(pattern, line):
                            if '-n' in flags:
                                matching_lines.append(f"{file}:{i+1}:{line}")
                            else:
                                matching_lines.append(f"{file}:{line}")
        return matching_lines
    else:
        return lines