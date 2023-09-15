import re

def parse_header(line):
    level = len(line) - len(line.lstrip('#'))
    if level > 6:
        return f'<p>{line}</p>'
    return f'<h{level}>{line[level + 1:].strip()}</h{level}>'

def parse_list(line):
    content = line.lstrip('* ')
    content = parse_emphasis(content)
    return f'<li>{content}</li>'

def parse_emphasis(line):
    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    return line

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        if line.startswith('#'):
            line = parse_header(line)
        elif line.startswith('*'):
            line = parse_list(line)
            if not in_list:
                in_list = True
                line = '<ul>' + line
        else:
            if in_list:
                res += '</ul>'
                in_list = False
            line = parse_emphasis(line)
            if not line.startswith('<h'):
                line = f'<p>{line}</p>'

        res += line

    if in_list:
        res += '</ul>'

    return res
