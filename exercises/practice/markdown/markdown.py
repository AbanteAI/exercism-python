import re


def parse(markdown):
    def parse_header(line):
        level = 0
        while line.startswith('#'):
            level += 1
            line = line[1:]
        if level > 6:
            return line.strip(), False
        return f'<h{level}>{line.strip()}</h{level}>', True if level > 0 else False

    def parse_list_item(line):
        return f'<li>{line[2:].strip()}</li>', True if line.startswith('* ') else False

    def parse_paragraph(line):
        return f'<p>{line.strip()}</p>', True if line.strip() else False

    def parse_bold(line):
        while '__' in line:
            start = line.find('__')
            end = line.find('__', start + 2)
            line = line[:start] + '<strong>' + line[start + 2:end] + '</strong>' + line[end + 2:]
        return line

    def parse_italic(line):
        while '_' in line:
            start = line.find('_')
            end = line.find('_', start + 1)
            line = line[:start] + '<em>' + line[start + 1:end] + '</em>' + line[end + 1:]
        return line

    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for line in lines:
        parsed_line, matched = parse_header(line)
        if not matched:
            parsed_line, matched = parse_list_item(line)
            if matched:
                if not in_list:
                    in_list = True
                    parsed_line = '<ul>' + parsed_line
                else:
                    if