import re

def abbreviate(words):
    words = re.sub(r"[^\w\s-]", "", words)
    acronym = ''.join(word[0].upper() for word in words.split())
    return acronym
