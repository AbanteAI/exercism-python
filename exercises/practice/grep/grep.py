import re

def grep(pattern, flags, files):
    results = []
    flag_set = set(flags)

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        for index, line in enumerate(lines):
            match = re.search(pattern, line, re.IGNORECASE if '-i' in flag_set else 0)

            if ('-v' in flag_set and not match) or ('-v' not in flag_set and match):
                if '-x' in flag_set and match and match.group() != line.rstrip():
                    continue

                output = ''

                if len(files) > 1:
                    output += f"{file}:"

                if '-n' in flag_set:
                    output += f"{index + 1}:"

                if '-l' not in flag_set:
                    output += line.rstrip()

                results.append(output)

                if '-l' in flag_set:
                    break
