import re


def parse_header(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i + ' '):
            return f'<h{i}>{line[i+1:].strip()}</h{i}>'
    return None if line.startswith('#') else line

def parse_list_item(line):
    if line.startswith('* '):
        return f'<li>{line[2:]}</li>'
    return None

def parse_bold(text):
    return re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)

def parse_italic(text):
    return re.sub(r'_(.*?)_', r'<em>\1</em>', text)

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        header = parse_header(line)
        if header is not None:
            if in_list:
                res += '</ul>'
                in_list = False
            res += header if header.startswith('<h') else f'<p>{header}</p>'
            continue

        list_item = parse_list_item(line)
        if list_item:
            if not in_list:
                res += '<ul>'
                in_list = True
            list_item = parse_bold(list_item)
            list_item = parse_italic(list_item)
            res += list_item
            continue

        if not in_list:
            line = parse_bold(line)
            line = parse_italic(line)
            res += f'<p>{line}</p>'

    if in_list:
        res += '</ul>'

    return res
    return res
