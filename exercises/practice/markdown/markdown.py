import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        line = parse_headers(line)
        line, in_list, in_list_append = parse_list_items(line, in_list, in_list_append)
        line = parse_paragraph(line)
        res += line
    if in_list:
        res += '</ul>'
    return res

def parse_headers(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i + ' '):
            return f'<h{i}>{line[i+1:]}</h{i}>'
    return line

def parse_list_items(line, in_list, in_list_append):
    if line.startswith('* '):
        line = line[2:]
        if not in_list:
            in_list = True
            line = '<ul><li>' + line
        else:
            line = '<li>' + line
        return line, in_list, in_list_append
    else:
        if in_list:
            in_list_append = True
            line = '</ul>' + line
        return line, in_list, in_list_append

def parse_paragraph(line):
    if not line.startswith(('<h', '<ul', '<p', '<li')):
        line = '<p>' + line + '</p>'
    line = parse_emphasis(line, '__', 'strong')
    line = parse_emphasis(line, '_', 'em')
    return line

def parse_emphasis(line, delimiter, tag):
    parts = line.split(delimiter)
    if len(parts) > 1 and len(parts) % 2 == 1:
        for i in range(1, len(parts), 2):
            parts[i] = f'<{tag}>{parts[i]}</{tag}>'
        line = delimiter.join(parts)
    return line
