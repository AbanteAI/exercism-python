import re

def grep(pattern, flags, files):
    matching_lines = []
    
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            
            for line_number, line in enumerate(lines, start=1):
                match = re.search(pattern, line, flags=flags)
                
                if match:
                    if '-n' in flags:
                        line = f"{file}:{line_number}:{line}"
                    else:
                        line = f"{file}:{line}"
                    
                    matching_lines.append(line)
    
    if '-l' in flags:
        matching_files = set(line.split(':')[0] for line in matching_lines)
        matching_lines = list(matching_files)
    
    if '-v' in flags:
        all_lines = set(file + ':' + line for file in files for line in open(file))
        non_matching_lines = all_lines - set(matching_lines)
        matching_lines = list(non_matching_lines)
    
    return matching_lines