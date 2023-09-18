def grep(pattern, flags, files):
    result = []
    flag_n = "-n" in flags
    flag_l = "-l" in flags
    flag_i = "-i" in flags
    flag_v = "-v" in flags
    flag_x = "-x" in flags

    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, start=1):
            line_stripped = line.strip()
            match = pattern in line_stripped
            if flag_i:
                match = pattern.lower() in line_stripped.lower()
            if flag_x:
                match = pattern == line_stripped
            if flag_v:
                match = not match

            if match:
                if flag_l:
                    result.append(file)
                    break
                else:
                    output_line = ""
                    if len(files) > 1:
                        output_line += f"{file}:"
                    if flag_n:
                        output_line += f"{i}:"
                    output_line += line_stripped
                    result.append(output_line)

    return "\n".join(result) + "\n" if result else ""