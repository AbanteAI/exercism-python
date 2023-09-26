# Removed unused import statement


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        if line.startswith('#'):
            header_level = line.count('#')
            line = f'<h{header_level}>{line.strip("# ")}</h{header_level}>'
        elif line.startswith('*'):
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = line[2:]
                if '__' in curr:
                    curr = curr.replace('__', '<strong>', 1).replace('__', '</strong>', 1)
                    is_bold = True
                if '_' in curr:
                    curr = curr.replace('_', '<em>', 1).replace('_', '</em>', 1)
                    is_italic = True
                line = f'<ul><li>{curr}</li>'
            else:
                is_bold = False
                is_italic = False
                curr = line[2:]
                if '__' in curr:
                    is_bold = True
                if '_' in curr:
                    is_italic = True
                if is_bold:
                    curr = curr.replace('__', '<strong>', 1).replace('__', '</strong>', 1)
                if is_italic:
                    curr = curr.replace('_', '<em>', 1).replace('_', '</em>', 1)
                line = f'<li>{curr}</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        if not any(tag in line for tag in ['<h', '<ul', '<p', '<li']):
            line = f'<p>{line}</p>'
        line = line.replace('__', '<strong>').replace('_', '<em>')

        if in_list_append:
            line = f'</ul>{line}'
            in_list_append = False
        res += line

    if in_list:
        res += '</ul>'
    return res