import re
def grep(pattern, flags, files):
    results = []
    flag_options = flags.split()

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        for index, line in enumerate(lines, start=1):
            if "-i" in flag_options:
                match = re.search(pattern, line, re.IGNORECASE)
            else:
                match = re.search(pattern, line)

            if match:
                if "-v" in flag_options:
                    continue

                if "-x" in flag_options:
                    if match.group() != line.strip():
                        continue

                if "-l" in flag_options:
                    results.append(file + "\n")
                    break
                elif "-n" in flag_options:
                    results.append(f"{file}:{index}:{line}")
                else:
                    results.append(f"{file}:{line}")
            elif "-v" in flag_options:
                results.append(f"{file}:{line}")

    return "".join(results)
