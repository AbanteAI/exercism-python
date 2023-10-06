import re

def parse_header(line):
    level = 0
    while line.startswith('#'):
        level += 1
        line = line[1:]
    if level > 6:
        return f'<p>#{line.strip()}</p>'
    return f'<h{level}>{line.strip()}</h{level}>'

def parse_list(line):
    line = line.lstrip('* ')
    line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
    return line

def parse_text(line):
    line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
    return f'<p>{line}</p>'

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        if line.startswith('#'):
            line = parse_header(line)
        elif line.startswith('*'):
            parsed_line = parse_list(line)
            if not in_list:
                in_list = True
                line = f'<ul><li>{parsed_line}</li>'
            else:
                line = f'<li>{parsed_line}</li>'
        else:
            if in_list:
                res += '</ul>'
                in_list = False
            line = parse_text(line)
        res += line
    if in_list:
        res += '</ul>'
    return res