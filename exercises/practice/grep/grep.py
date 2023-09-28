def grep(pattern, flags, files):
    results = []
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                line = line.strip()
                if "-i" in flags:
                    search_pattern = pattern.lower()
                    line_content = line.lower()
                else:
                    search_pattern = pattern
                    line_content = line
                if "-x" in flags:
                    match = search_pattern == line_content
                else:
                    match = search_pattern in line_content
                if "-v" in flags:
                    match = not match
                if match:
                    if "-l" in flags:
                        results.append(file)
                        break
                    else:
                        output = line
                        if "-n" in flags:
                            output = f"{index + 1}:{output}"
                        if len(files) > 1:
                            output = f"{file}:{output}"
                        results.append(output)
    return "\n".join(results) + "\n" if results else ""