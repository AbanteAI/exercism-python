import re
import argparse
def grep(pattern, flags, files):
    results = []

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if flags and "-i" in flags:
                    search_pattern = re.compile(pattern, re.IGNORECASE)
                else:
                    search_pattern = re.compile(pattern)
                
                if re.search(search_pattern, line):
                    result = ""
                    if flags and "-l" in flags:
                        result = file
                    elif flags and "-n" in flags:
                        result = f"{file}:{index + 1}:{line.strip()}"
                    else:
                        result = line.strip()
                    results.append(result)

    return "\n".join(results)
def main():
    parser = argparse.ArgumentParser(description='Search for a pattern in files')
    parser.add_argument('pattern', type=str, help='Pattern to search for')
    parser.add_argument('files', type=str, nargs='+', help='Files to search')
    args = parser.parse_args()

    results = grep(args.pattern, None, args.files)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()