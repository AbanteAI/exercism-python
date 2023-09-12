import re
def grep(pattern, flags, files):
    result = []
    flag_list = flags.split()
    line_number_flag = "-n" in flag_list
    case_insensitive_flag = "-i" in flag_list
    print_file_name_flag = "-l" in flag_list
    match_entire_line_flag = "-x" in flag_list
    inverted_flag = "-v" in flag_list

    def match_line(line):
        if case_insensitive_flag:
            line = line.lower()
            pattern_lower = pattern.lower()
        else:
            pattern_lower = pattern

        if match_entire_line_flag:
            match = re.fullmatch(pattern_lower, line.strip())
        else:
            match = re.search(pattern_lower, line)

        return not match if inverted_flag else match

    for file_name in files:
        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if match_line(line):
                    prefix = f"{file_name}:"
                    if print_file_name_flag:
                        result.append(prefix.strip())
                        break
                    if line_number_flag:
                        prefix += f"{line_number}:"
                    result.append(f"{prefix}{line}")

    return "".join(result)