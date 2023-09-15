import re


import re

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for line in lines:
        # Handle headers
        if line.startswith('#'):
            header_level = line.count('#')
            header_text = line.strip('# ')
            line = f"<h{header_level}>{header_text}</h{header_level}>"

        # Handle lists
        elif line.startswith('*'):
            list_item = line.strip('* ')
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                m = re.match('(.*)__(.*)__(.*)', list_item)
                if m:
                    list_item = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
                    is_bold = True
                m = re.match('(.*)_(.*)_(.*)', list_item)
                if m:
                    list_item = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
                    is_italic = True
                line = f"<ul><li>{list_item}</li>"
            else:
                is_bold = False
                is_italic = False
                m = re.match('(.*)__(.*)__(.*)', list_item)
                if m:
                    is_bold = True
                m = re.match('(.*)_(.*)_(.*)', list_item)
                if m:
                    is_italic = True
                if is_bold:
                    list_item = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
                if is_italic:
                    list_item = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
                line = f"<li>{list_item}</li>"
        else:
            if in_list:
                in_list_append = True
                in_list = False

        # Handle paragraphs
        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = f"<p>{line}</p>"

        # Handle bold and italic
        m = re.match('(.*)__(.*)__(.*)', line)
        if m:
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', line)
        if m:
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)

        if in_list_append:
            line = '</ul>' + line
            in_list_append = False

        res += line

    if in_list:
        res += '</ul>'

    return res
