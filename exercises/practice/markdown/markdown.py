import re


import re

def parse_header(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i + ' '):
            return f'<h{i}>{line[i+1:].strip()}</h{i}>'
    return None

def parse_list_item(line):
    m = re.match(r'\* (.*)', line)
    if m:
        return '<li>' + parse_bold_italic(m.group(1)) + '</li>'
    return None

def parse_bold_italic(text):
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    return text

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        header = parse_header(line)
        if header is not None:
            res += header
            continue

        list_item = parse_list_item(line)
        if list_item:
            if not in_list:
                res += '<ul>'
            res += list_item
            in_list = True
            continue
        else:
            if in_list:
                res += '</ul>'
                in_list = False

        if not header and not re.match('<h|<ul|<p|<li', line):
            line = '<p>' + parse_bold_italic(line) + '</p>'
        res += line

    if in_list:
        res += '</ul>'
    return res
