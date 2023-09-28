import re


def parse_header(line):
    for i in range(7, 0, -1):
        if line.startswith("#" * i):
            if i > 6:
                return None
            return f"<h{i}>{line[i + 1:]}</h{i}>"
    return None


def parse_list_item(line):
    if line.startswith("* "):
        return f"<li>{line[2:]}</li>"
    return None


def parse_paragraph(line):
    return f"<p>{line}</p>"


def parse_bold(text):
    return text.replace("__", "<strong>", 1).replace("__", "</strong>", 1)


def parse_italic(text):
    return text.replace("_", "<em>", 1).replace("_", "</em>", 1)


def parse_line(line):
    header = parse_header(line)
    if header:
        return header

    list_item = parse_list_item(line)
    if list_item:
        return list_item

    return parse_paragraph(line)


def parse(markdown):
    lines = markdown.split('\n')
    html = []
    in_list = False

    for line in lines:
        line_html = parse_line(line)

        if line.startswith("* "):
            if not in_list:
                in_list = True
                html.append("<ul>")
        elif in_list:
            in_list = False
            html.append("</ul>")

        line_html = parse_bold(line_html)
        line_html = parse_italic(line_html)

        html.append(line_html)

    if in_list:
        html.append("</ul>")

    return "".join(html)