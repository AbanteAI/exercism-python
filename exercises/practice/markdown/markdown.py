import re


class MarkdownParser:
    def __init__(self):
        self.in_list = False
        self.in_list_append = False
        self.result = ''

    def parse(self, markdown):
        lines = markdown.split('\n')
        for line in lines:
            line = self.parse_line(line)
            self.result += line
        self.close_list_if_needed()
        return self.result

        if self.is_list_item(line):
            return self.parse_list_item(line)
        if self.in_list:
            self.close_list()
        return self.parse_paragraph(line)
    def parse_line(self, line):
        if self.is_heading(line):
            return self.parse_heading(line)
        if self.in_list:
            if not self.is_list_item(line):
                self.close_list()
                return self.parse_paragraph(line)
            return self.parse_list_item(line)
        return self.parse_paragraph(line)

    def is_heading(self, line):
        return re.match('#+ ', line)

    def parse_heading(self, line):
        level = len(re.match('#+', line).group(0))
        content = line[level+1:]
        if level <= 6:
            return f'<h{level}>{content}</h{level}>'
        else:
            return f'<p>{line}</p>'

    def is_list_item(self, line):
        return re.match(r'\* (.*)', line)

    def parse_list_item(self, line):
        content = re.match(r'\* (.*)', line).group(1)
        content = self.parse_text(content)
        if not self.in_list:
            self.start_list()
        return f'<li>{content}</li>'

    def start_list(self):
        self.in_list = True
        self.result += '<ul>'

    def close_list(self):
        self.in_list = False
        self.in_list_append = False
        self.result += '</ul>'

    def close_list_if_needed(self):
        if self.in_list:
            self.close_list()

    def parse_paragraph(self, line):
        line = self.parse_text(line)
        return f'<p>{line}</p>'

    def parse_text(self, text):
        text = self.parse_bold(text)
        text = self.parse_italic(text)
        return text

    def parse_bold(self, text):
        return re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)

    def parse_italic(self, text):
        return re.sub(r'_(.*?)_', r'<em>\1</em>', text)


def parse(markdown):
    parser = MarkdownParser()
    return parser.parse(markdown)
