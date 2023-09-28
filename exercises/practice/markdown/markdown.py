import re


import re

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for line in lines:
        # Handle headers
        for i in range(6, 0, -1):
            if re.match(f'{"#" * i} (.*)', line):
                line = f'<h{i}>{line[i+1:]}</h{i}>'
                break

        # Handle list items
        m = re.match(r'\* (.*)', line)
        if m:
            curr = m.group(1)
            is_bold = False
            is_italic = False

            # Check for bold and italic formatting
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                curr = f'{m1.group(1)}<strong>{m1.group(2)}</strong>{m1.group(3)}'
                is_bold = True
            m1 = re.match('(.*)_(.*)_(.*)', curr)
            if m1:
                curr = f'{m1.group(1)}<em>{m1.group(2)}</em>{m1.group(3)}'
                is_italic = True

            # Add list item tags
            if not in_list:
                in_list = True
                line = f'<ul><li>{curr}</li>'
            else:
                if is_bold:
                    curr = f'{m1.group(1)}<strong>{m1.group(2)}</strong>{m1.group(3)}'
                if is_italic:
                    curr = f'{m1.group(1)}<em>{m1.group(2)}</em>{m1.group(3)}'
                line = f'<li>{curr}</li>'
        else:
            # Handle paragraphs
            if in_list:
                in_list_append = True
                in_list = False
            m = re.match('<h|<ul|<p|<li', line)
            if not m:
                line = f'<p>{line}</p>'

        # Handle bold and italic formatting
        m = re.match('(.*)__(.*)__(.*)', line)
        if m:
            line = f'{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}'
        m = re.match('(.*)_(.*)_(.*)', line)
        if m:
            line = f'{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}'

        # Append line to result
        if in_list_append:
            line = f'</ul>{line}'
            in_list_append = False
        res += line

    if in_list:
        res += '</ul>'

    return res
