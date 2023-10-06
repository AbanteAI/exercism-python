import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        line = parse_headers(line)
        line = parse_list_items(line, in_list)
        line = parse_paragraph(line, in_list, in_list_append)
        res += line
    if in_list:
        res += '</ul>'
    return res

def parse_headers(line):
    for i in range(6, 0, -1):
        if line.startswith('#' * i + ' '):
            line = f'<h{i}>{line[i+1:]}</h{i}>'
            break
    return line

def parse_list_items(line, in_list):
    match = re.match(r'\* (.*)', line)
    if match:
        curr = match.group(1)
        curr = parse_formatting(curr)
        if not in_list:
            line = '<ul><li>' + curr + '</li>'
        else:
            line = '<li>' + curr + '</li>'
    return line

    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)

def parse_paragraph(line, in_list, in_list_append):
    match = re.match('<h|<ul|<p|<li', line)
    if not match:
        line = '<p>' + line + '</p>'
    if in_list_append:
        line = '</ul>' + line
    return line



















    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)