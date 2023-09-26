

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        for j in range(6, 0, -1):
            if re.match(f'{"#" * j} (.*)', i) is not None:
                i = f'<h{j}>{i[j+1:]}</h{j}>'
                break
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = f'{m1.group(1)}<strong>{m1.group(2)}</strong>{m1.group(3)}'
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = f'{m1.group(1)}<em>{m1.group(2)}</em>{m1.group(3)}'
                    is_italic = True
                i = f'<ul><li>{curr}</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = f'{m1.group(1)}<strong>{m1.group(2)}</strong>{m1.group(3)}'
                if is_italic:
                    curr = f'{m1.group(1)}<em>{m1.group(2)}</em>{m1.group(3)}'
                i = f'<li>{curr}</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = f'<p>{i}</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = f'{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}'
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = f'{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}'
        if in_list_append:
            i = f'</ul>{i}'
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
