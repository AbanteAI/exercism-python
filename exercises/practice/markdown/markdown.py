import re


def parse_header(line):
    """Parse markdown headers and return the corresponding HTML."""
    for i in range(6, 0, -1):
        header_pattern = '^' + '#' * i + ' (.*)'
        match = re.match(header_pattern, line)
        if match:
            return f'<h{i}>{match.group(1)}</h{i}>'
    if line.startswith('#'):
        return f'<p>{line}</p>'
    return None

def parse_list_item(line):
    """Parse markdown list items and return the corresponding HTML."""
    if line.startswith('* '):
        return f'<li>{line[2:]}</li>'
    return None

def parse_bold(text):
    """Parse markdown bold syntax and return the corresponding HTML."""
    bold_pattern = re.compile(r'__(.*?)__')
    return bold_pattern.sub(r'<strong>\1</strong>', text)

def parse_italic(text):
    """Parse markdown italic syntax and return the corresponding HTML."""
    italic_pattern = re.compile(r'_(.*?)_')
    return italic_pattern.sub(r'<em>\1</em>', text)

def parse_paragraph(line):
    """Parse markdown paragraphs and return the corresponding HTML."""
    if not line.startswith(('<h', '<ul', '<p', '<li')):
        return f'<p>{line}</p>'
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
        
        line = parse_bold(line)
        line = parse_italic(line)
        
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
