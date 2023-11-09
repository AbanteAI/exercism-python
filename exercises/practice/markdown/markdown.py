import re


def parse_header(line):
    """Parse markdown headers and return the corresponding HTML."""
    for i in range(6, 0, -1):
        if line.startswith('#' * i + ' '):
            return f'<h{i}>{line[i+1:].strip()}</h{i}>'
    if line.startswith('#'):
        return '<p>' + line + '</p>'
    return None

def parse_list_item(line):
    """Parse markdown list items and return the corresponding HTML."""
    m = re.match(r'\* (.*)', line)
    if m:
        return '<li>' + parse_text(m.group(1)) + '</li>'
    return None

def parse_bold(text):
    """Parse markdown bold text and return the corresponding HTML."""
    m = re.match('(.*)__(.*)__(.*)', text)
    if m:
        return m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return text

def parse_italic(text):
    """Parse markdown italic text and return the corresponding HTML."""
    m = re.match('(.*)_(.*)_(.*)', text)
    if m:
        return m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return text

def parse_text(text):
    """Parse markdown text and return the corresponding HTML."""
    text = parse_bold(text)
    text = parse_italic(text)
    return text

def parse_paragraph(line):
    """Parse markdown paragraphs and return the corresponding HTML."""
    if not re.match('<h|<ul|<p|<li', line):
        return '<p>' + parse_text(line) + '</p>'
    return line
def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        header = parse_header(line)
        if header:
            line = header
        else:
            list_item = parse_list_item(line)
            if list_item:
                if not in_list:
                    in_list = True
                    line = '<ul>' + list_item
                else:
                    line = list_item
            else:
                if in_list:
                    in_list_append = True
                    in_list = False
                line = parse_paragraph(line)
                if in_list_append:
                    line = '</ul>' + line
                    in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
